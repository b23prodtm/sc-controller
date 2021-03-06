#!/usr/bin/env python
from collections import OrderedDict
from cheader import defines

HW_SCANS = {
	# HW_SCANS are used by uinput
	'KEY_ESC':			0x70029,
	'KEY_F1':			0x7003a,
	'KEY_F2':			0x7003b,
	'KEY_F3':			0x7003c,
	'KEY_F4':			0x7003d,
	'KEY_F5':			0x7003e,
	'KEY_F6':			0x7003f,
	'KEY_F7':			0x70040,
	'KEY_F8':			0x70041,
	'KEY_F9':			0x70042,
	'KEY_F10':			0x70043,
	'KEY_F11':			0x70044,
	'KEY_F12':			0x70045,
	'KEY_SYSRQ':		0x70046,
	'KEY_SCROLLLOCK':	0x70047,
	'KEY_PAUSE':		0x70048,
	'KEY_GRAVE':		0x70035,
	'KEY_1':			0x7001e,
	'KEY_2':			0x7001f,
	'KEY_3':			0x70020,
	'KEY_4':			0x70021,
	'KEY_5':			0x70022,
	'KEY_6':			0x70023,
	'KEY_7':			0x70024,
	'KEY_8':			0x70025,
	'KEY_9':			0x70026,
	'KEY_0':			0x70027,
	'KEY_MINUS':		0x7002d,
	'KEY_EQUAL':		0x7002e,
	'KEY_BACKSPACE':	0x7002a,
	'KEY_TAB':			0x7002b,
	'KEY_Q':			0x70014,
	'KEY_W':			0x7001a,
	'KEY_E':			0x70008,
	'KEY_R':			0x70015,
	'KEY_T':			0x70017,
	'KEY_Y':			0x7001c,
	'KEY_U':			0x70018,
	'KEY_I':			0x7000c,
	'KEY_O':			0x70012,
	'KEY_P':			0x70013,
	'KEY_LEFTBRACE':	0x7002f,
	'KEY_RIGHTBRACE':	0x70030,
	'KEY_ENTER':		0x70028,
	'KEY_CAPSLOCK':		0x70039,
	'KEY_A':			0x70004,
	'KEY_S':			0x70016,
	'KEY_D':			0x70007,
	'KEY_F':			0x70009,
	'KEY_G':			0x7000a,
	'KEY_H':			0x7000b,
	'KEY_J':			0x7000d,
	'KEY_K':			0x7000e,
	'KEY_L':			0x7000f,
	'KEY_SEMICOLON':	0x70033,
	'KEY_APOSTROPHE':	0x70034,
	'KEY_BACKSLASH':	0x70032,
	'KEY_LEFTSHIFT':	0x700e1,
	'KEY_102ND':		0x70064,
	'KEY_Z':			0x7001d,
	'KEY_X':			0x7001b,
	'KEY_C':			0x70006,
	'KEY_V':			0x70019,
	'KEY_B':			0x70005,
	'KEY_N':			0x70011,
	'KEY_M':			0x70010,
	'KEY_COMMA':		0x70036,
	'KEY_DOT':			0x70037,
	'KEY_SLASH':		0x70038,
	'KEY_RIGHTSHIFT':	0x700e5,
	'KEY_LEFTCTRL':		0x700e0,
	'KEY_LEFTMETA':		0x700e3,
	'KEY_LEFTALT':		0x700e2,
	'KEY_SPACE':		0x7002c,
	'KEY_RIGHTALT':		0x700e6,
	'KEY_RIGHTMETA':	0x700e7,
	'KEY_COMPOSE':		0x70065,
	'KEY_RIGHTCTRL':	0x700e4,
	'KEY_INSERT':		0x70049,
	'KEY_HOME':			0x7004a,
	'KEY_PAGEUP':		0x7004b,
	'KEY_DELETE':		0x7004c,
	'KEY_END':			0x7004d,
	'KEY_PAGEDOWN':		0x7004e,
	'KEY_UP':			0x70052,
	'KEY_LEFT':			0x70050,
	'KEY_DOWN':			0x70051,
	'KEY_RIGHT':		0x7004f,
	'KEY_NUMLOCK':		0x70053,
	'KEY_KPSLASH':		0x70054,
	'KEY_KPASTERISK':	0x70055,
	'KEY_KPMINUS':		0x70056,
	'KEY_KP7':			0x7005f,
	'KEY_KP8':			0x70060,
	'KEY_KP9':			0x70061,
	'KEY_KPPLUS':		0x70057,
	'KEY_KP4':			0x7005c,
	'KEY_KP5':			0x7005d,
	'KEY_KP6':			0x7005e,
	'KEY_KP1':			0x70059,
	'KEY_KP2':			0x7005a,
	'KEY_KP3':			0x7005b,
	'KEY_KPENTER':		0x70058,
	'KEY_KP0':			0x70062,
	'KEY_KPDOT':		0x70063,
	'KEY_CONFIG':		0xc0183,
	'KEY_PLAYPAUSE':	0xc00cd,
	'KEY_MUTE':			0xc00e2,
	'KEY_VOLUMEDOWN':	0xc00ea,
	'KEY_VOLUMEUP':		0xc00e9,
	'KEY_HOMEPAGE':		0xc0223,
	'KEY_PREVIOUSSONG':	0xc00f0,
	'KEY_NEXTSONG':		0xc00f1,
	'KEY_BACK':			0xc00f2,
	'KEY_FORWARD':		0xc00f3,
}

X11_SCANS = {
	# Generated by pressing everything in xev
	'KEY_ESC':			9,
	'KEY_1':			10,
	'KEY_2':			11,
	'KEY_3':			12,
	'KEY_4':			13,
	'KEY_5':			14,
	'KEY_6':			15,
	'KEY_7':			16,
	'KEY_8':			17,
	'KEY_9':			18,
	'KEY_0':			19,
	'KEY_MINUS':		20,
	'KEY_EQUAL':		21,
	'KEY_BACKSPACE':	22,
	'KEY_TAB':			23,
	'KEY_Q':			24,
	'KEY_W':			25,
	'KEY_E':			26,
	'KEY_R':			27,
	'KEY_T':			28,
	'KEY_Y':			29,
	'KEY_U':			30,
	'KEY_I':			31,
	'KEY_O':			32,
	'KEY_P':			33,
	'KEY_LEFTBRACE':	34,
	'KEY_RIGHTBRACE':	35,
	'KEY_ENTER':		36,
	'KEY_KPENTER':		104,
	'KEY_LEFTCTRL':		37,
	'KEY_RIGHTCTRL':	105,
	'KEY_A':			38,
	'KEY_S':			39,
	'KEY_D':			40,
	'KEY_F':			41,
	'KEY_G':			42,
	'KEY_H':			43,
	'KEY_J':			44,
	'KEY_K':			45,
	'KEY_L':			46,
	'KEY_SEMICOLON':	47,
	'KEY_APOSTROPHE':	48,
	'KEY_GRAVE':		49,
	'KEY_BACKSLASH':	51,
	'KEY_LEFTSHIFT':	50,
	'KEY_102ND':		61,
	'KEY_Z':			52,
	'KEY_X':			53,
	'KEY_C':			54,
	'KEY_V':			55,
	'KEY_B':			56,
	'KEY_N':			57,
	'KEY_M':			58,
	'KEY_COMMA':		59,
	'KEY_DOT':			60,
	'KEY_SLASH':		61,
	'KEY_KPSLASH':		106,
	'KEY_RIGHTSHIFT':	62,
	'KEY_SYSRQ':		107,
	'KEY_KPASTERISK':	63,
	'KEY_LEFTALT':		64,
	'KEY_RIGHTALT':		108,
	'KEY_SPACE':		65,
	'KEY_CAPSLOCK':		66,
	'KEY_F1':			67,
	'KEY_F2':			68,
	'KEY_F3':			69,
	'KEY_F4':			70,
	'KEY_F5':			71,
	'KEY_F6':			72,
	'KEY_F7':			73,
	'KEY_F8':			74,
	'KEY_F9':			75,
	'KEY_F10':			76,
	'KEY_F11':			95,
	'KEY_F12':			96,
	'KEY_NUMLOCK':		77,
	'KEY_PAUSE':		127,
	'KEY_SCROLLLOCK':	78,
	'KEY_UP':			111,
	'KEY_PAGEUP':		112,
	'KEY_LEFT':			113,
	'KEY_RIGHT':		114,
	'KEY_END':			115,
	'KEY_DOWN':			116,
	'KEY_PAGEDOWN':		117,
	'KEY_INSERT':		118,
	'KEY_DELETE':		119,
	'KEY_KPMINUS':		82,
	'KEY_KPPLUS':		86,
	'KEY_LEFTMETA':		133,
	'KEY_RIGHTMETA':	134,
	'KEY_COMPOSE':		135,
}

WIN32_SCANS = {
	# Source: http://www.quadibloc.com/comp/scan.htm
	'KEY_ESC':			0x01,
	'KEY_1':			0x02,
	'KEY_2':			0x03,
	'KEY_3':			0x04,
	'KEY_4':			0x05,
	'KEY_5':			0x06,
	'KEY_6':			0x07,
	'KEY_7':			0x08,
	'KEY_8':			0x09,
	'KEY_9':			0x0A,
	'KEY_0':			0x0B,
	'KEY_MINUS':		0x0C,
	'KEY_EQUAL':		0x0D,
	'KEY_BACKSPACE':	0x0E,
	'KEY_TAB':			0x0F,
	'KEY_Q':			0x10,
	'KEY_W':			0x11,
	'KEY_E':			0x12,
	'KEY_R':			0x13,
	'KEY_T':			0x14,
	'KEY_Y':			0x15,
	'KEY_U':			0x16,
	'KEY_I':			0x17,
	'KEY_O':			0x18,
	'KEY_P':			0x19,
	'KEY_LEFTBRACE':	0x1A,
	'KEY_RIGHTBRACE':	0x1B,
	'KEY_ENTER':		0x1C,
	'KEY_KPENTER':		0xE01C,
	'KEY_LEFTCTRL':		0x1D,
	'KEY_RIGHTCTRL':	0xE01D,
	'KEY_A':			0x1E,
	'KEY_S':			0x1F,
	'KEY_D':			0x20,
	'KEY_F':			0x21,
	'KEY_G':			0x22,
	'KEY_H':			0x23,
	'KEY_J':			0x24,
	'KEY_K':			0x25,
	'KEY_L':			0x26,
	'KEY_SEMICOLON':	0x27,
	'KEY_APOSTROPHE':	0x28,
	'KEY_BACKSLASH':	0x29,
	'KEY_LEFTSHIFT':	0x2A,
	'KEY_102ND':		0x2B,
	'KEY_Z':			0x2C,
	'KEY_X':			0x2D,
	'KEY_C':			0x2E,
	'KEY_V':			0x2F,
	'KEY_B':			0x30,
	'KEY_N':			0x31,
	'KEY_M':			0x32,
	'KEY_COMMA':		0x33,
	'KEY_DOT':			0x34,
	'KEY_SLASH':		0x35,
	# KEY_KPSLASH 0x35+
	'KEY_RIGHTSHIFT':	0x36,
	'KEY_SYSRQ':		0x37,
	# KEY_KPASTERISK 0x37+
	# PrtSc 37/54+
	'KEY_LEFTALT':		0x38,
	'KEY_RIGHTALT':		0xE038,
	'KEY_SPACE':		0x39,
	'KEY_CAPSLOCK':		0x3A,
	'KEY_F1':			0x3B,
	'KEY_F2':			0x3C,
	'KEY_F3':			0x3D,
	'KEY_F4':			0x3E,
	'KEY_F5':			0x3F,
	'KEY_F6':			0x40,
	'KEY_F7':			0x41,
	'KEY_F8':			0x42,
	'KEY_F9':			0x43,
	'KEY_F10':			0x44,
	'KEY_F11':			0x57,
	'KEY_F12':			0x58,
	'KEY_KP7':			0x47,
	'KEY_KP8':			0x48,
	'KEY_KP9':			0x49,
	'KEY_KP4':			0x4B,
	'KEY_KP5':			0x4C,
	'KEY_KP6':			0x4D,
	'KEY_KP1':			0x4F,
	'KEY_KP2':			0x50,
	'KEY_KP3':			0x51,
	'KEY_KP0':			0x52,
	'KEY_KPDOT':		0x53,
	'KEY_NUMLOCK':		0x45, # +
	'KEY_PAUSE':		0x46, # 45/46+
	# KEY_SCROLLLOCK 46+
	# Home KP 0x47
	'KEY_UP':			0xE048,
	'KEY_PAGEUP':		0xE049,
	'KEY_LEFT':			0xE04B,
	'KEY_RIGHT':		0xE04D,
	'KEY_END':			0xE04F,
	'KEY_DOWN':			0xE050,
	'KEY_PAGEDOWN':		0xE051,
	'KEY_INSERT':		0xE052,
	'KEY_DELETE':		0xE053,
	'KEY_KPMINUS':		0x4A,
	'KEY_KPPLUS':		0x4E,
	'KEY_LEFTMETA':		0xE05B,
	'KEY_RIGHTMETA':	0xE05C,
	'KEY_COMPOSE':		0xE05D,
}

WIN32_VKs = {
	# Source: https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
	'KEY_ESC':			0x1B,
	'KEY_GRAVE':		0xC0,
	'KEY_0':			0x30,
	'KEY_1':			0x31,
	'KEY_2':			0x32,
	'KEY_3':			0x33,
	'KEY_4':			0x34,
	'KEY_5':			0x35,
	'KEY_6':			0x36,
	'KEY_7':			0x37,
	'KEY_8':			0x38,
	'KEY_9':			0x39,
	'KEY_MINUS':		0xBF,
	'KEY_EQUAL':		0xDF,
	'KEY_BACKSPACE':	0x08,
	'KEY_TAB':			0x09,
	'KEY_A':			0x41,
	'KEY_B':			0x42,
	'KEY_C':			0x43,
	'KEY_D':			0x44,
	'KEY_E':			0x45,
	'KEY_F':			0x46,
	'KEY_G':			0x47,
	'KEY_H':			0x48,
	'KEY_I':			0x49,
	'KEY_J':			0x4A,
	'KEY_K':			0x4B,
	'KEY_L':			0x4C,
	'KEY_M':			0x4D,
	'KEY_N':			0x4E,
	'KEY_O':			0x4F,
	'KEY_P':			0x50,
	'KEY_Q':			0x51,
	'KEY_R':			0x52,
	'KEY_S':			0x53,
	'KEY_T':			0x54,
	'KEY_U':			0x55,
	'KEY_V':			0x56,
	'KEY_W':			0x57,
	'KEY_X':			0x58,
	'KEY_Y':			0x59,
	'KEY_Z':			0x5A,
	'KEY_KP0':			0x60,
	'KEY_KP1':			0x61,
	'KEY_KP2':			0x62,
	'KEY_KP3':			0x63,
	'KEY_KP4':			0x64,
	'KEY_KP5':			0x65,
	'KEY_KP6':			0x66,
	'KEY_KP7':			0x67,
	'KEY_KP8':			0x68,
	'KEY_KP9':			0x69,
	'KEY_LEFTBRACE':	0xDB,
	'KEY_RIGHTBRACE':	0xDD,
	'KEY_ENTER':		0x0D,
	# 'KEY_102ND':
	'KEY_LEFTCTRL':		0x11,
	'KEY_RIGHTCTRL':	0xa3,
	'KEY_SEMICOLON':	0xBA,
	'KEY_APOSTROPHE':	0xDE,
	'KEY_BACKSLASH':	0xDC,
	'KEY_LEFTSHIFT':	0x10,
	'KEY_RIGHTSHIFT':	0xA1,
	'KEY_COMMA':		0xBC,
	'KEY_DOT':			0xBD,
	'KEY_SLASH':		0xBE,
	'KEY_SYSRQ':		0x2C,
	'KEY_SCROLLLOCK':	0x91,
	'KEY_PAUSE':		0x13,
	# 'KEY_NUMLOCK':
	'KEY_KPSLASH':		0x6F,
	'KEY_KPASTERISK':	0x6A,
	'KEY_KPMINUS':		0x6D,
	'KEY_KPPLUS':		0x6B,
	# 'KEY_KPENTER':
	'KEY_LEFTALT':		0x12,
	# 'KEY_RIGHTALT':
	'KEY_SPACE':		0x20,
	'KEY_CAPSLOCK':		0x14,
	'KEY_F1':			0x70,
	'KEY_F2':			0x71,
	'KEY_F3':			0x72,
	'KEY_F4':			0x73,
	'KEY_F5':			0x74,
	'KEY_F6':			0x75,
	'KEY_F7':			0x76,
	'KEY_F8':			0x77,
	'KEY_F9':			0x78,
	'KEY_F10':			0x79,
	'KEY_F11':			0x7A,
	'KEY_F12':			0x7B,
	'KEY_END':			0x23,
	'KEY_HOME':			0x24,
	'KEY_INSERT':		0x2D,
	'KEY_DELETE':		0x2E,
	'KEY_PAGEUP':		0x21,
	'KEY_PAGEDOWN':		0x22,
	'KEY_UP':			0x26,
	'KEY_LEFT':			0x25,
	'KEY_RIGHT':		0x27,
	'KEY_DOWN':			0x28,
	'KEY_LEFTMETA':		0x5B,
	'KEY_RIGHTMETA':	0x5C,
	'KEY_COMPOSE':		0x5D,
}

NUMBERS = {
	# Values are assigned when generating to make sure it is bellow 1st button
	# and out of (0, ABS_CNT) range.
	"YAW",
	"ROLL",
}


def is_rel_or_abs(x):	# or button
	return "_" in x and x.split("_", 1)[0] in ("ABS", "BTN", "REL")


def unindent(number, s):
	def un(n, line):
		while n > 0 and line and line[0] == "\t":
			line, n = line[1:], n - 1
		return line
	
	return "\n".join([ un(number, x) for x in s.split("\n") ]).strip("\n")


class Item:
	def __init__(self, name, value=-1):
		self.name = name
		self.value = value
		self.hw_scan = 0
		self.x11_keycode = 0
		self.win32_scan = 0
		self.win32_vk = 0
	
	def __repr__(self):
		if self.name:
			return '{ %i,\t%s, %s, %s, %s, %s }' % (
				self.value, '"%s"' % (self.name,),
				hex(self.hw_scan).upper().replace("0X", "0x"),
				hex(self.x11_keycode).upper().replace("0X", "0x"),
				hex(self.win32_scan).upper().replace("0X", "0x"),
				hex(self.win32_vk).upper().replace("0X", "0x"),
			)
		else:
			return '{ %i }' % (self.value,)


def generate(chead):
	everything = {}
	
	for x in chead:
		if "KEY_" in x and x not in ("KEY_CNT", "KEY_MAX"):
			everything[x] = Item(x)
			everything[x].value = chead[x]
	for x in HW_SCANS:
		everything[x].hw_scan = HW_SCANS[x]
	for x in X11_SCANS:
		everything[x].x11_keycode = X11_SCANS[x]
	for x in WIN32_SCANS:
		everything[x].win32_scan = WIN32_SCANS[x]
	for x in WIN32_VKs:
		everything[x].win32_vk = WIN32_VKs[x]
		
	key_max = max([ a.value for a in everything.values() ])
	key_max = 256		# TODO: Removing all above this; Those keys are probably not
						# TODO: used on desktop anyway, so I'll see what will this break
	values = { a.value: a for a in everything.values() }
	while key_max and (key_max not in values or not values[key_max].name):
		key_max -= 1
	
	for (i, x) in enumerate(NUMBERS):
		everything[x] = Item(x)
		everything[x].value = i + chead["ABS_CNT"] + 1
	
	output = open("generated.c", "w")
	print >>output, unindent(2, """
		/*
		 * SC Controller - Autogenerated mapping of KEY_* constants to everything
		 * This is used by uinput, its emulation, parser and by OSD.
		 *
		 * ========= THIS FILE IS AUTOGENERATED ==========
		 *
		 * Generated by generate-constants.py from include/scc/input-event-codes.h
		 * and some hardcoded maps.
		 */
		#include "scc/utils/hashmap.h"
		#include "scc/utils/assert.h"
		#include "scc/input-event-codes.h"
		#include "conversions.h"
		#include <unistd.h>
		#include <stdint.h>
		
		""")
	
	print >>output, ""
	print >>output, "const uint16_t SCC_KEYCODE_MAX = %s;" % (key_max,)
	print >>output, ""
	
	print >>output, unindent(2, """
		struct Item keys[] = {
		""")
	
	for x in xrange(key_max + 1):
		if x not in values:
			values[x] = Item("", x)
		print >>output, "\t%s," % (values[x],)
	
	print >>output, unindent(2, """};
		
		struct Item rels_and_abses[] = {
		""")
	
	all_numbers = NUMBERS.union(set(( x for x in chead if is_rel_or_abs(x) )))
	sort_key = lambda a: chead[a] if a in chead else everything[a].value
	for x in sorted(all_numbers, key=sort_key):
		print >>output, "\t%s," % (Item(x, sort_key(x)),)
	
	print >>output, "};";
	print >>output, "size_t rels_and_abses_cnt = sizeof(rels_and_abses) / sizeof(struct Item);";


if __name__ == '__main__':
	chead = OrderedDict()
	for path, filename in [
			('../../include/scc/', 'controller.h'),
			('../../include/scc/', 'input-event-codes.h'),
			('../../include/scc/', 'rel-event-codes.h')]:
		chead.update(defines(path, filename))
	
	generate(chead)

