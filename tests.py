import hashlib, unittest
import pickle, random
import bz2, numtxt


##def gen_data():
##    '''generates data for testing
##    run only once and when code is proper'''
##    data = {}
##
##    functions = {'conway-wechsler': '_conway',
##                 'noll': '_noll', 'rowlett': '_rowlett',
##                 'knuth': '_knuth'}
##
##    # naming functions
##    for mthd in numtxt.methods:
##        numtxt.setMethod(mthd)
##        call = functions[mthd]
##        data[mthd] = {}
##
##        if 'conway' in mthd or 'noll' in mthd:
##            for styl in numtxt.suffix_styles:
##                numtxt.setStyle(styl)
##                data[mthd][styl] = {}
##
##                func = getattr(numtxt, call)
##                for i in range(10001):
##                    data[mthd][styl][i] = func(i)
##
##                for i in range(5, 35):
##                    j = 1000 ** i
##                    data[mthd][styl][j + 1] = func(j + 1)
##
##        elif 'rowlett' in mthd:
##            numtxt.setStyle('short')
##
##            func = getattr(numtxt, call)
##            for i in range(1000):
##                data[mthd][i] = func(i)
##
##        elif 'knuth' in mthd:
##            numtxt.setStyle('short')
##
##            func = getattr(numtxt, call)
##            for i in range(2501):
##                data[mthd][i] = func(i, is_log=True)
##
##            for i in range(1001):
##                j = 2 ** i
##                data[mthd][j] = func(j, is_log=True)
##
##    # general functions
##    numtxt.setMethod('conway-wechsler')
##    numtxt.setStyle('short')
##
##    data['name'] = {True: {}, False: {}}
##    for i in range(100):
##        data['name'][True][i] = numtxt.name(i, True)
##        data['name'][False][i] = numtxt.name(i, False)
##
##    data['ordinal'] = {True: {}, False: {}}
##    for i in range(100):
##        data['ordinal'][True][i] = numtxt.ordinal(i, True)
##        data['ordinal'][False][i] = numtxt.ordinal(i, False)
##
##    data['approx'] = {'num': {}, 'str': {}}
##    for i in range(500):
##        r = random.randint(-1000**500, 1000**500)
##        data['approx']['num'][r] = numtxt.approx(r)
##
##        rr = (random.randint(-500, 500) +
##              [0, random.random()][random.randint(0, 1)])
##        q = str(rr)
##        data['approx']['str'][q] = numtxt.approx(q)
##
##    return data
##
##def dump_and_hash(path, data):
##    "saves and prints out hash of data file"
##    with bz2.BZ2File(path, 'wb') as dmp:
##        pickle.dump(data, dmp, 2)
##
##    hsh = hashlib.sha1()
##    with open(path, 'rb') as dmp:
##        hsh.update(dmp.read())
##    print(hsh.hexdigest())
##
##dump_and_hash('test_data.dmp', gen_data())


class testNumtxt(unittest.TestCase):
    longMessage = True

    data_path = 'test_data.dmp'  # load data
    with bz2.BZ2File(data_path, 'rb') as src:
        data = pickle.load(src)

    def test_data_integrity(self):
        hsh = hashlib.sha1()
        with open(self.data_path, 'rb') as src:
            hsh.update(src.read())
        chksum = '3a6a1b796e14e21f998445ca3d9dcbe9df87dfac'
        mesg = 'test data might be invalid, check {}.'.format(self.data_path)
        #mesg += ' (if only this test fails, checksum is out of date)'
        self.assertEqual(hsh.hexdigest(), chksum, mesg)

    ## -- CONWAY-WECHSLER --
    def test_conway_short(self):
        mthd, sty = 'conway-wechsler', 'short'
        values = self.data[mthd][sty]
        numtxt.setMethod(mthd)
        numtxt.setStyle(sty)

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt._conway(inp)

            mesg = '{} {} form failed with input {}'.format(mthd, sty, inp)
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    def test_conway_long(self):
        mthd, sty = 'conway-wechsler', 'long'
        values = self.data[mthd][sty]
        numtxt.setMethod(mthd)
        numtxt.setStyle(sty)

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt._conway(inp)

            mesg = '{} {} form failed with input {}'.format(mthd, sty, inp)
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    def test_conway_british(self):
        mthd, sty = 'conway-wechsler', 'british'
        values = self.data[mthd][sty]
        numtxt.setMethod(mthd)
        numtxt.setStyle(sty)

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt._conway(inp)

            mesg = '{} {} form failed with input {}'.format(mthd, sty, inp)
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    ## -- NOLL --
    def test_noll_short(self):
        mthd, sty = 'noll', 'short'
        values = self.data[mthd][sty]
        numtxt.setMethod(mthd)
        numtxt.setStyle(sty)

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt._noll(inp)

            mesg = '{} {} form failed with input {}'.format(mthd, sty, inp)
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    def test_noll_long(self):
        mthd, sty = 'noll', 'long'
        values = self.data[mthd][sty]
        numtxt.setMethod(mthd)
        numtxt.setStyle(sty)

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt._noll(inp)

            mesg = '{} {} form failed with input {}'.format(mthd, sty, inp)
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    def test_noll_british(self):
        mthd, sty = 'noll', 'british'
        values = self.data[mthd][sty]
        numtxt.setMethod(mthd)
        numtxt.setStyle(sty)

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt._noll(inp)

            mesg = '{} {} form failed with input {}'.format(mthd, sty, inp)
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    ## -- ROWLETT --
    def test_rowlett(self):
        mthd = 'rowlett'
        values = self.data[mthd]
        numtxt.setMethod(mthd)
        numtxt.setStyle('short')

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt._rowlett(inp)

            mesg = '{} form failed with input {}'.format(mthd, inp)
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    ## -- KNUTH --
    def test_knuth(self):
        mthd = 'knuth'
        values = self.data[mthd]
        numtxt.setMethod(mthd)
        numtxt.setStyle('short')

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt._knuth(inp, is_log=True)

            mesg = '{} form failed with input {}, is_log=True'.format(mthd,inp)
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    ## -- APPROX --
    def test_approx_num(self):
        numtxt.setMethod('conway-wechsler')
        numtxt.setStyle('short')
        values = self.data['approx']['num']

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt.approx(inp)

            mesg = ('approx (conway-wechsler, short)' +
                    ' failed with input {}'.format(inp))
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    def test_approx_str(self):
        numtxt.setMethod('conway-wechsler')
        numtxt.setStyle('short')
        values = self.data['approx']['str']

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt.approx(inp)

            mesg = ('approx func (conway-wechsler, short)' +
                    ' failed with input \'{}\''.format(inp))
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    ## -- NAME --
    def test_name_A(self):
        numtxt.setMethod('conway-wechsler')
        numtxt.setStyle('short')
        values = self.data['name'][True]

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt.name(inp, True)

            mesg = ('name func (conway-wechsler, short)' +
                    ' failed with input {}, condensed=True'.format(inp))
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    def test_name_B(self):
        numtxt.setMethod('conway-wechsler')
        numtxt.setStyle('short')
        values = self.data['name'][False]

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt.name(inp, False)

            mesg = ('name func (conway-wechsler, short)' +
                    ' failed with input {}, condensed=False'.format(inp))
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    ## -- ORDINAL --
    def test_ordinal_A(self):
        numtxt.setMethod('conway-wechsler')
        numtxt.setStyle('short')
        values = self.data['ordinal'][True]

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt.ordinal(inp, True)

            mesg = ('ordinal func (conway-wechsler, short)' +
                    ' failed with input {}, short=True'.format(inp))
            self.assertEqual(tst_outp, act_outp, msg=mesg)

    def test_ordinal_B(self):
        numtxt.setMethod('conway-wechsler')
        numtxt.setStyle('short')
        values = self.data['ordinal'][False]

        for inp in values.keys():
            tst_outp = values[inp]
            act_outp = numtxt.ordinal(inp, False)

            mesg = ('ordinal func (conway-wechsler, short)' +
                    ' failed with input {}, short=False'.format(inp))
            self.assertEqual(tst_outp, act_outp, msg=mesg)


if __name__ == '__main__':
    unittest.main(verbosity=1)
