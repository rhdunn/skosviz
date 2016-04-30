#!/usr/bin/python

# Copyright (C) 2010-2016 Reece H. Dunn
#
# This file is part of skosviz.
#
# skosviz is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# skosviz is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with skosviz.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import difflib

class TestSuite:
	def __init__(self, name, args):
		self.passed = 0
		self.failed = 0
		self.name = name
		if len(args) == 2:
			self.run_only = args[1]
		else:
			self.run_only = None

	def check_command(self, filename, expect, test_expect, format):
		tmpfile = '/tmp/skosviz-test-result.txt'

		sys.stdout.write('testing %s as %s ... ' % (filename, format))

		os.system('%s -f %s "%s" -o %s' % (
			os.path.join(sys.path[0], '..', 'skosviz'),
			format,
			os.path.join(sys.path[0], filename),
			tmpfile))

		with open(os.path.join(sys.path[0], expect), 'r') as f:
			expected = [ repr(x) for x in f.read().split('\n') if not x == '' ]

		with open(tmpfile, 'r') as f:
			got      = [ repr(x) for x in f.read().split('\n') if not x == '' ]

		if test_expect == 'expect-pass':
			ret = expected == got
		else:
			ret = expected != got

		if ret:
			self.passed = self.passed + 1
			print 'passed [%s]' % test_expect
		else:
			self.failed = self.failed + 1
			print 'failed [%s]' % test_expect

		if not ret or test_expect == 'expect-fail':
			print '    %s' % ('>'*75)
			for line in difflib.unified_diff(expected, got, fromfile='expected', tofile='got'):
				print '    | %s' % line.replace('\n', '')
			print '    %s' % ('<'*75)

	def run(self, tests):
		for test in tests:
			if 'text' in test.keys():
				self.check_command(
					filename=test['filename'],
					expect=test['text'],
					test_expect='expect-pass',
					format='text')
			elif 'dot' in test.keys():
				self.check_command(
					filename=test['filename'],
					expect=test['dot'],
					test_expect='expect-pass',
					format='dot')
			else:
				self.failed = self.failed + 1
				print 'unknown handler for test case %s' % test

	def summary(self):
		print
		print '========== summary of the %s test results ==========' % self.name
		print '  %s passed' % str(self.passed).rjust(4)
		print '  %s failed' % str(self.failed).rjust(4)
		print '  %s total'  % str(self.passed + self.failed).rjust(4)
		print
		if self.failed != 0:
			raise Exception('Some of the tests failed.')

testcases = [
	{'filename': 'skos-core/ConceptScheme-dc-title.rdf', 'text': 'skos-core/ConceptScheme-dc-title.txt'},
	{'filename': 'skos-core/ConceptScheme-dc-title.rdf', 'dot': 'skos-core/ConceptScheme-dc-title.dot'},
	{'filename': 'skos-core/ConceptScheme-dct-title.rdf', 'text': 'skos-core/ConceptScheme-dc-title.txt'},
	{'filename': 'skos-core/ConceptScheme-dct-title.rdf', 'dot': 'skos-core/ConceptScheme-dc-title.dot'},
	{'filename': 'rdfxml/skos-hasTopConcept.rdf', 'text': 'rdfxml/skos-hasTopConcept.txt'},
	{'filename': 'rdfxml/skos-altLabel.rdf',      'text': 'rdfxml/skos-altLabel.txt'},
	{'filename': 'rdfxml/skos-narrower.rdf',      'text': 'rdfxml/skos-narrower.txt'},
]

test = TestSuite('skosviz', args=sys.argv)
test.run(testcases)
test.summary()
