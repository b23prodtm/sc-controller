/**
 * SC-Controller - constants
 *
 * Methods for converting between various constants
 */
#include "scc/controller.h"
#include "scc/tools.h"
#include <string.h>


SCButton scc_what_to_pressed_button(PadStickTrigger what) {
	switch (what) {
	case PST_LEFT:
		return B_LPAD;
	case PST_RIGHT:
		return B_RPAD;
	case PST_CPAD:
		return B_CPADPRESS;
	case PST_STICK:
		return B_STICKPRESS;
	case PST_GYRO:
		break;
	}
	return 0;
}

SCButton scc_what_to_touch_button(PadStickTrigger what) {
	switch (what) {
	case PST_LEFT:
		return B_LPADTOUCH;
	case PST_RIGHT:
		return B_RPADTOUCH;
	case PST_CPAD:
		return B_CPADTOUCH;
	case PST_STICK:
	case PST_GYRO:
		break;
	}
	return 0;
}

SCButton scc_string_to_button(const char* s) {
	switch (s[0]) {
	case 'R':
		if (0 == strcmp("RB", s)) return B_RB;
		if (0 == strcmp("RT", s)) return B_RT;
		if (0 == strcmp("RGRIP", s)) return B_RGRIP;
		if (0 == strcmp("RPADTOUCH", s)) return B_RPADTOUCH;
		if (0 == strcmp("RPADPRESS", s)) return B_RPAD;
		break;
	case 'L':
		if (0 == strcmp("LB", s)) return B_LB;
		if (0 == strcmp("LT", s)) return B_LT;
		if (0 == strcmp("LGRIP", s)) return B_LGRIP;
		if (0 == strcmp("LPADTOUCH", s)) return B_LPADTOUCH;
		if (0 == strcmp("LPADPRESS", s)) return B_LPAD;
		break;
	case 'S':
		if (0 == strcmp("START", s)) return B_START;
		if (0 == strcmp("STICKPRESS", s)) return B_STICKPRESS;
		break;
	case 'C':
		if (0 == strcmp("C", s)) return B_C;
		if (0 == strcmp("CPADTOUCH", s)) return B_CPADTOUCH;
		if (0 == strcmp("CPADPRESS", s)) return B_CPADPRESS;
		break;
	case 'B':
		if (0 == strcmp("B", s)) return B_B;
		if (0 == strcmp("BACK", s)) return B_BACK;
		break;
	default:
		if (0 == strcmp("A", s)) return B_A;
		if (0 == strcmp("X", s)) return B_X;
		if (0 == strcmp("Y", s)) return B_Y;
	}
	return 0;
}

PadStickTrigger scc_string_to_pst(const char* s) {
	switch (s[0]) {
	case 'R':
		if (0 == strcmp("RIGHT", s)) return PST_RIGHT;
		break;
	case 'L':
		if (0 == strcmp("LEFT", s)) return PST_LEFT;
		break;
	case 'S':
		if (0 == strcmp("STICK", s)) return PST_STICK;
		break;
	case 'G':
		if (0 == strcmp("GYRO", s)) return PST_GYRO;
		break;
	}
	return 0;
}

const char* scc_what_to_string(PadStickTrigger what) {
	switch (what) {
	case PST_LEFT:		return "LEFT";
	case PST_RIGHT:		return "RIGHT";
	case PST_CPAD:		return "CPAD";
	case PST_STICK:		return "STICK";
	case PST_GYRO:		return "GYRO";
	}
	return NULL;
}

const char* scc_button_to_string(SCButton b) {
	switch (b) {
	case B_RPADTOUCH:	return "RPADTOUCH";
	case B_LPADTOUCH:	return "LPADTOUCH";
	case B_RPAD:		return "RPAD";
	case B_LPAD:		return "LPAD";
	case B_RGRIP:		return "RGRIP";
	case B_LGRIP:		return "LGRIP";
	case B_START:		return "START";
	case B_C:			return "C";
	case B_BACK:		return "BACK";
	case B_A:			return "A";
	case B_X:			return "X";
	case B_B:			return "B";
	case B_Y:			return "Y";
	case B_LB:			return "LB";
	case B_RB:			return "RB";
	case B_LT:			return "LT";
	case B_RT:			return "RT";
	case B_CPADTOUCH:	return "CPADTOUCH";
	case B_CPADPRESS:	return "CPADPRESS";
	case B_STICKPRESS:	return "STICKPRESS";
	default:
		return NULL;
	}
}
