# needs lex installed to compile ltp
import test
from autotest_utils import *

class ltp(test.test):
	version = 1

	# http://prdownloads.sourceforge.net/ltp/ltp-full-20060412.tgz
	def setup(self, tarball = 'ltp-full-20060412.tgz'):
		tarball = unmap_url(self.bindir, tarball, self.tmpdir)
		extract_tarball_to_dir(tarball, self.srcdir)
		os.chdir(self.srcdir)

		system('make -j %d' % count_cpus())
		system('yes n | make install')

	# Note: to run a specific test, try '-f test' in the args
	# eg, job.runtest(None, 'ltp', '-f ballista')
	def execute(self, args = ''):
		logfile = self.resultsdir + '/ltp.log'
		args = '-q -l ' + logfile + ' ' + args
		system(self.srcdir + '/runltp ' + args)
