#!/usr/bin/env python2
# Copyright (c) 2015 Stany MARCEL <stanypub@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from scc.constants import HapticPos
import logging

log = logging.getLogger("SCController")


class Controller(object):
	"""
	Base class for all controller drivers. Implementations are in
	scc.dricvers package.
	
	Derived class should implement every method from here.
	"""
	def __init__(self):
		self.mapper = None
	
	
	def set_mapper(self, mapper):
		""" Sets mapper for controller """
		self.mapper = mapper
	
	
	def get_mapper(self):
		""" Returns mapper set for controller """
		return self.mapper
	
	
	def set_led_level(self, level):
		"""
		Configures LED intensity, if supported.
		'level' goes from 0.0 to 100.0
		"""
		pass
	
	
	def set_gyro_enabled(self, enabled):
		""" Enables or disables gyroscope, if supported """
		pass
	
	
	def turnoff(self):
		""" Turns off controller, if supported """
		pass
	

class HapticData(object):
	""" Simple container to hold haptic feedback settings """
	
	def __init__(self, position, amplitude=512, frequency=4, period=1024, count=1):
		"""
		'frequency' is used only when emulating touchpad and describes how many
		pixels should mouse travell between two feedback ticks.
		"""
		data = tuple([ int(x) for x in (position, amplitude, period, count) ])
		if data[0] not in (HapticPos.LEFT, HapticPos.RIGHT, HapticPos.BOTH):
			raise ValueError("Invalid position")
		for i in (1,2,3):
			if data[i] > 0x8000 or data[i] < 0:
				raise ValueError("Value out of range")
		# frequency is multiplied by 1000 just so I don't have big numbers everywhere;
		# it's float until here, so user still can make pad squeak if he wish
		frequency = int(max(1.0, frequency * 1000.0))
		
		self.data = data				# send to controller
		self.frequency = frequency		# used internally
	
	
	def with_position(self, position):
		""" Creates copy of HapticData with position value changed """
		trash, amplitude, period, count = self.data
		return HapticData(position, amplitude, self.frequency, period, count)
	
	
	def get_position(self):
		return HapticPos(self.data[0])
	
	def get_amplitude(self):
		return self.data[1]
	
	def get_frequency(self):
		return float(self.frequency) / 1000.0
	
	def get_period(self):
		return self.data[2]
	
	def get_count(self):
		return self.data[3]
	
	def __mul__(self, by):
		"""
		Allows multiplying HapticData by scalar to get same values
		with increased amplitude.
		"""
		position, amplitude, period, count = self.data
		amplitude = min(amplitude * by, 0x8000)
		return HapticData(position, amplitude, self.frequency, period, count)
