#pragma once
#include <stdint.h>
#ifdef __linux__
#include <linux/input-event-codes.h>
#else
#include "scc/input-event-codes.h"
#endif

typedef struct Controller Controller;
typedef struct ControllerInput ControllerInput;
typedef struct Mapper Mapper;
typedef struct HapticData HapticData;


typedef enum ControllerFlags {
	// uint32
	CF_NO_FLAGS			= 0,		// No flags means Steam Controller
	CF_HAS_RSTICK		= 1 << 0,	// Controller has right stick instead of touchpad
	CF_SEPARATE_STICK	= 1 << 1,	// Left stick and left pad are using separate axes
	// EUREL_GYROS is set when syro sensor values are provided as pitch, yaw
	// and roll instead of quaterion. 'q4' is unused in such case.
	CF_EUREL_GYROS		= 1 << 2,
	CF_HAS_CPAD			= 1 << 3,	// Controller has DS4-like touchpad in center
	CF_HAS_DPAD			= 1 << 4,	// Controller has normal d-pad instead of touchpad
	CF_NO_GRIPS			= 1 << 5,	// Controller has no grips
} ControllerFlags;

struct Controller {
	void				(*deallocate)(Controller* c);
	ControllerFlags		flags;
	/**
	 * Returns controller ID which should be unique, short string with no spaces,
	 * situable as key in configuration.
	 *
	 * ID _has_ to be unique for every active controller at any given time
	 * and it's prefferable for it to stay same for same physical controller
	 * if it's disconnected and then reconnected again. For example, serial
	 * number is good thing to derive ID from.
	 *
	 * Caller should not have to deallocate returned string and returned value
	 * has to be be kept in memory at least until controller is deallocate()'d.
	 */
	const char*			(*get_id)(Controller* c);
	/**
	 * Returns type identifier - short string with no spaces describing 
	 * type of controller. This string should be unique for each driver.
	 *
	 * String is used by GUI to assign icons and, along with id, to store
	 * controller settings.
	 *
	 * Caller should not have to deallocate returned string and returned value
	 * has to be be kept in memory at least until controller is deallocate()'d.
	 */
	const char*			(*get_type)(Controller* c);
	/**
	 * get_description should return string description of Controller suitable
	 * for logging, for example "<SCByCable FDXXYYZZ>".
	 *
	 * Caller should not have to deallocate returned string and returned value
	 * has to be be kept in memory at least until controller is deallocate()'d.
	 */
	const char*			(*get_description)(Controller* c);
	/**
	 * Returns file name of json file that GUI can use to load more data about
	 * controller (background image, button images, available buttons and
	 * axes, etc...) File name may be absolute path or just basename of file in
	 * /usr/share/scc
	 *
	 * Returns NULL if there is no configuration file. GUI will use defaults
	 * in such case.
	 * Alternativelly, this method may point to NULL. That will have same effect
	 * as having method and returning NULL from it.
	 *
	 * Caller should not have to deallocate returned string and returned value
	 * has to be be kept in memory at least until controller is deallocate()'d.
	 */
	const char*			(*get_gui_config_file)(Controller* c);
	/**
	 * Plays haptic effect. This callback may be set to NULL if controller has
	 * no rumble support.
	 */
	void				(*haptic_effect)(Controller* c, HapticData* hdata);
	/**
	 * Flushes pending controller outputs, if any. If non-NULL, this is guaranteed
	 * to be called repeadedly, at least after every call to mapper->input.
	 */
	void				(*flush)(Controller* c, Mapper* m);
	/**
	 * Turns the controller off. This will most likely be unsupported by most
	 * of controllers and so method may be set to NULL.
	 */
	void				(*turnoff)(Controller* c);
	/**
	 * Sets Mapper for this controller. May set NULL in which case controller
	 * should not send any input events.
	 */
	void				(*set_mapper)(Controller* c, Mapper* m);
};


typedef uint16_t Axis;
typedef uint16_t Keycode;

typedef uint8_t TriggerValue;
typedef int16_t AxisValue;
typedef int16_t GyroValue;

typedef enum SCButton {
	B_RPADTOUCH			= 0b0010000000000000000000000000000,
	B_LPADTOUCH			= 0b0001000000000000000000000000000,
	B_RPAD				= 0b0000100000000000000000000000000,
	B_LPAD				= 0b0000010000000000000000000000000,
	B_RGRIP				= 0b0000001000000000000000000000000,
	B_LGRIP				= 0b0000000100000000000000000000000,
	B_START				= 0b0000000010000000000000000000000,
	B_C					= 0b0000000001000000000000000000000,
	B_BACK				= 0b0000000000100000000000000000000,
	B_A					= 0b0000000000000001000000000000000,
	B_X					= 0b0000000000000000100000000000000,
	B_B					= 0b0000000000000000010000000000000,
	B_Y					= 0b0000000000000000001000000000000,
	B_LB				= 0b0000000000000000000100000000000,
	B_RB				= 0b0000000000000000000010000000000,
	B_LT				= 0b0000000000000000000001000000000,
	B_RT				= 0b0000000000000000000000100000000,
	// CPADTOUCH and CPADPRESS is used only on DS4 pad
	B_CPADTOUCH			= 0b0000000000000000000000000000100,
	B_CPADPRESS			= 0b0000000000000000000000000000010,
	B_STICKPRESS		= 0b1000000000000000000000000000000,
	_SCButton_padding = 0xFFFFFFFF	// uint32_t
} SCButton;

struct ControllerInput {
	SCButton			buttons;
	TriggerValue		ltrig;
	TriggerValue		rtrig;
	AxisValue			stick_x;
	AxisValue			stick_y;
	AxisValue			lpad_x;
	AxisValue			lpad_y;
	AxisValue			rpad_x;
	AxisValue			rpad_y;
	AxisValue			cpad_x;
	AxisValue			cpad_y;
	GyroValue			gpitch;
	GyroValue			groll;
	GyroValue			gyaw;
	GyroValue			q1;
	GyroValue			q2;
	GyroValue			q3;
	GyroValue			q4;
};

typedef enum PadStickTrigger {
	PST_LEFT			= 1,			// This is constant for both left pad and left trigger
	PST_RIGHT			= 2,			// This is constant for both right pad and right trigger
	PST_CPAD			= 3,
	PST_STICK			= 4,
	PST_GYRO			= 5,
} PadStickTrigger;

#define SCC_DEFAULT		0xFF			/* This is used by menus for both SCButton and PadStickTrigger values */
#define SCC_SAME		0xFE			/* This is used by menus for both SCButton and PadStickTrigger values */
#define SCC_True		0x01			/* This is used only by generate-parser-constants script */
#define SCC_False		0x00			/* This is used only by generate-parser-constants script */

typedef enum HapticPos {
	HAPTIC_RIGHT		= 0,
	HAPTIC_LEFT			= 1,
	HAPTIC_BOTH			= 2,
} HapticPos;

struct HapticData {
	HapticPos			pos;
	uint16_t			amplitude;
	float				frequency;
	uint16_t			period;
};

#define HAPTIC_ENABLED(h) ((h)->amplitude != 0)
#define HAPTIC_DISABLE(h) do {		\
		(h)->period = 0;			\
		(h)->amplitude = 0;			\
		(h)->frequency = 0;			\
	} while (0)

#define STICK_PAD_MIN		((AxisValue)-0x8000)
#define STICK_PAD_MAX		((AxisValue) 0x7FFF)
#define STICK_PAD_MIN_HALF	((AxisValue)-0x4000)
#define STICK_PAD_MAX_HALF	((AxisValue) 0x3FFF)

#define TRIGGER_MIN			((TriggerValue)0)
#define TRIGGER_HALF		((TriggerValue)50)
// TRIGGER_CLICK is value on which trigger clicks
#define TRIGGER_CLICK		((TriggerValue)254)
#define TRIGGER_MAX			((TriggerValue)255)
#define NO_AXIS				((Axis)(REL_MAX + 1))
