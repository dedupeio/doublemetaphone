# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

from doublemetaphone import doublemetaphone


class MetaphoneTestCase(unittest.TestCase):
    """
    """
    def test_single_result(self):
        result = doublemetaphone(u"aubrey")
        self.assertEqual(result, ('APR', 'APR'))

    def test_double_result(self):
        result = doublemetaphone(u"richard")
        self.assertEqual(result, ('RXRT', 'RKRT'))

    def test_general_word_list(self):
        result = doublemetaphone('Jose')
        self.assertEqual(result, ('HS', 'HS'))
        result = doublemetaphone('cambrillo')
        self.assertEqual(result, ('KMPRL', 'KMPR'))
        result = doublemetaphone('otto')
        self.assertEqual(result, ('AT', 'AT'))
        result = doublemetaphone('aubrey')
        self.assertEqual(result, ('APR', 'APR'))
        result = doublemetaphone('maurice')
        self.assertEqual(result, ('MRS', 'MRS'))
        result = doublemetaphone('auto')
        self.assertEqual(result, ('AT', 'AT'))
        result = doublemetaphone('maisey')
        self.assertEqual(result, ('MS', 'MS'))
        result = doublemetaphone('catherine')
        self.assertEqual(result, ('K0RN', 'KTRN'))
        result = doublemetaphone('geoff')
        self.assertEqual(result, ('JF', 'KF'))
        result = doublemetaphone('Chile')
        self.assertEqual(result, ('XL', 'XL'))
        result = doublemetaphone('katherine')
        self.assertEqual(result, ('K0RN', 'KTRN'))
        result = doublemetaphone('steven')
        self.assertEqual(result, ('STFN', 'STFN'))
        result = doublemetaphone('zhang')
        self.assertEqual(result, ('JNK', 'JNK'))
        result = doublemetaphone('bob')
        self.assertEqual(result, ('PP', 'PP'))
        result = doublemetaphone('ray')
        self.assertEqual(result, ('R', 'R'))
        result = doublemetaphone('Tux')
        self.assertEqual(result, ('TKS', 'TKS'))
        result = doublemetaphone('bryan')
        self.assertEqual(result, ('PRN', 'PRN'))
        result = doublemetaphone('bryce')
        self.assertEqual(result, ('PRS', 'PRS'))
        result = doublemetaphone('Rapelje')
        self.assertEqual(result, ('RPL', 'RPL'))
        result = doublemetaphone('richard')
        self.assertEqual(result, ('RXRT', 'RKRT'))
        result = doublemetaphone('solilijs')
        self.assertEqual(result, ('SLLS', 'SLLS'))
        result = doublemetaphone('Dallas')
        self.assertEqual(result, ('TLS', 'TLS'))
        result = doublemetaphone('Schwein')
        self.assertEqual(result, ('XN', 'XFN'))
        result = doublemetaphone('dave')
        self.assertEqual(result, ('TF', 'TF'))
        result = doublemetaphone('eric')
        self.assertEqual(result, ('ARK', 'ARK'))
        result = doublemetaphone('Parachute')
        self.assertEqual(result, ('PRKT', 'PRKT'))
        result = doublemetaphone('brian')
        self.assertEqual(result, ('PRN', 'PRN'))
        result = doublemetaphone('randy')
        self.assertEqual(result, ('RNT', 'RNT'))
        result = doublemetaphone('Through')
        self.assertEqual(result, ('0R', 'TR'))
        result = doublemetaphone('Nowhere')
        self.assertEqual(result, ('NR', 'NR'))
        result = doublemetaphone('heidi')
        self.assertEqual(result, ('HT', 'HT'))
        result = doublemetaphone('Arnow')
        self.assertEqual(result, ('ARN', 'ARNF'))
        result = doublemetaphone('Thumbail')
        self.assertEqual(result, ('0MPL', 'TMPL'))

    def test_homophones(self):
        self.assertEqual(
            doublemetaphone(u"tolled"),
            doublemetaphone(u"told"))
        self.assertEqual(
            doublemetaphone(u"katherine"),
            doublemetaphone(u"catherine"))
        self.assertEqual(
            doublemetaphone(u"brian"),
            doublemetaphone(u"bryan"))

    def test_similar_names(self):
        #result = doublemetaphone("Bartoš")
        #self.assertEqual(result, ('PRTS', 'PRTS'))
        result = doublemetaphone(u"Bartosz")
        self.assertEqual(result, ('PRTS', 'PRTX'))
        result = doublemetaphone(u"Bartosch")
        self.assertEqual(result, ('PRTX', 'PRTX'))
        result = doublemetaphone(u"Bartos")
        self.assertEqual(result, ('PRTS', 'PRTS'))

        result = set(doublemetaphone(u"Jablonski")).intersection(
            doublemetaphone(u"Yablonsky"))
        self.assertEqual(list(result), ['APLNSK'])
        result = set(doublemetaphone(u"Smith")).intersection(
            doublemetaphone(u"Schmidt"))
        self.assertEqual(list(result), ['XMT'])

    def test_non_english_unicode(self):
        result = doublemetaphone("andestādītu")
        self.assertEqual(result, ('ANTSTTT', 'ANTSTTT'))

    #def test_c_cedilla(self):
    #    result = doublemetaphone("français")
    #    self.assertEqual(result, ('FRNS', 'FRNSS'))
    #    result = doublemetaphone("garçon")
    #    self.assertEqual(result, ('KRSN', ''))
    #    result = doublemetaphone("leçon")
    #    self.assertEqual(result, ('LSN', ''))

    def test_various_german(self):
        result = doublemetaphone("ach")
        self.assertEqual(result, ("AK", "AK"))
        result = doublemetaphone("bacher")
        self.assertEqual(result, ("PKR", "PKR"))
        result = doublemetaphone("macher")
        self.assertEqual(result, ("MKR", "MKR"))

    def test_various_italian(self):
        result = doublemetaphone("bacci")
        self.assertEqual(result, ("PX", "PX"))
        result = doublemetaphone("bertucci")
        self.assertEqual(result, ("PRTX", "PRTX"))
        result = doublemetaphone("bellocchio")
        self.assertEqual(result, ("PLX", "PLX"))
        result = doublemetaphone("bacchus")
        self.assertEqual(result, ("PKS", "PKS"))
        result = doublemetaphone("focaccia")
        self.assertEqual(result, ("FKX", "FKX"))
        result = doublemetaphone("chianti")
        self.assertEqual(result, ("KNT", "KNT"))
        result = doublemetaphone("tagliaro")
        self.assertEqual(result, ("TKLR", "TLR"))
        result = doublemetaphone("biaggi")
        self.assertEqual(result, ("PJ", "PK"))

    def test_various_spanish(self):
        result = doublemetaphone("bajador")
        self.assertEqual(result, ("PJTR", "PHTR"))
        result = doublemetaphone("cabrillo")
        self.assertEqual(result, ("KPRL", "KPR"))
        result = doublemetaphone("gallegos")
        self.assertEqual(result, ("KLKS", "KKS"))
        result = doublemetaphone("San Jacinto")
        self.assertEqual(result, ("SNHSNT", "SNHSNT"))

    def test_various_french(self):
        result = doublemetaphone("rogier")
        self.assertEqual(result, ("RJ", "RJR"))
        result = doublemetaphone("breaux")
        self.assertEqual(result, ("PR", "PR"))

    def test_various_slavic(self):
        result = doublemetaphone("Wewski")
        self.assertEqual(result, ("ASK", "FFSK"))

    def test_various_chinese(self):
        result = doublemetaphone("zhao")
        self.assertEqual(result, ("J", "J"))

    def test_dutch_origin(self):
        result = doublemetaphone("school")
        self.assertEqual(result, ("SKL", "SKL"))
        result = doublemetaphone("schooner")
        self.assertEqual(result, ("SKNR", "SKNR"))
        result = doublemetaphone("schermerhorn")
        self.assertEqual(result, ("XRMRRN", "SKRMRRN"))
        result = doublemetaphone("schenker")
        self.assertEqual(result, ("XNKR", "SKNKR"))

    def test_ch_words(self):
        result = doublemetaphone("Charac")
        self.assertEqual(result, ("KRK", "KRK"))
        result = doublemetaphone("Charis")
        self.assertEqual(result, ("KRS", "KRS"))
        result = doublemetaphone("chord")
        self.assertEqual(result, ("KRT", "KRT"))
        result = doublemetaphone("Chym")
        self.assertEqual(result, ("KM", "KM"))
        result = doublemetaphone("Chia")
        self.assertEqual(result, ("K", "K"))
        result = doublemetaphone("chem")
        self.assertEqual(result, ("KM", "KM"))
        result = doublemetaphone("chore")
        self.assertEqual(result, ("XR", "XR"))
        result = doublemetaphone("orchestra")
        self.assertEqual(result, ("ARKSTR", "ARKSTR"))
        result = doublemetaphone("architect")
        self.assertEqual(result, ("ARKTKT", "ARKTKT"))
        result = doublemetaphone("orchid")
        self.assertEqual(result, ("ARKT", "ARKT"))

    def test_cc_words(self):
        result = doublemetaphone("accident")
        self.assertEqual(result, ("AKSTNT", "AKSTNT"))
        result = doublemetaphone("accede")
        self.assertEqual(result, ("AKST", "AKST"))
        result = doublemetaphone("succeed")
        self.assertEqual(result, ("SKST", "SKST"))

    def test_mc_words(self):
        result = doublemetaphone("mac caffrey")
        self.assertEqual(result, ("MKFR", "MKFR"))
        result = doublemetaphone("mac gregor")
        self.assertEqual(result, ("MKRKR", "MKRKR"))
        result = doublemetaphone("mc crae")
        self.assertEqual(result, ("MKR", "MKR"))
        result = doublemetaphone("mcclain")
        self.assertEqual(result, ("MKLN", "MKLN"))

    def test_gh_words(self):
        result = doublemetaphone("laugh")
        self.assertEqual(result, ("LF", "LF"))
        result = doublemetaphone("cough")
        self.assertEqual(result, ("KF", "KF"))
        result = doublemetaphone("rough")
        self.assertEqual(result, ("RF", "RF"))

    def test_g3_words(self):
        result = doublemetaphone("gya")
        self.assertEqual(result, ("K", "J"))
        result = doublemetaphone("ges")
        self.assertEqual(result, ("KS", "JS"))
        result = doublemetaphone("gep")
        self.assertEqual(result, ("KP", "JP"))
        result = doublemetaphone("geb")
        self.assertEqual(result, ("KP", "JP"))
        result = doublemetaphone("gel")
        self.assertEqual(result, ("KL", "JL"))
        result = doublemetaphone("gey")
        self.assertEqual(result, ("K", "J"))
        result = doublemetaphone("gib")
        self.assertEqual(result, ("KP", "JP"))
        result = doublemetaphone("gil")
        self.assertEqual(result, ("KL", "JL"))
        result = doublemetaphone("gin")
        self.assertEqual(result, ("KN", "JN"))
        result = doublemetaphone("gie")
        self.assertEqual(result, ("K", "J"))
        result = doublemetaphone("gei")
        self.assertEqual(result, ("K", "J"))
        result = doublemetaphone("ger")
        self.assertEqual(result, ("KR", "JR"))
        result = doublemetaphone("danger")
        self.assertEqual(result, ("TNJR", "TNKR"))
        result = doublemetaphone("manager")
        self.assertEqual(result, ("MNKR", "MNJR"))
        result = doublemetaphone("dowager")
        self.assertEqual(result, ("TKR", "TJR"))

    def test_pb_words(self):
        result = doublemetaphone("Campbell")
        self.assertEqual(result, ("KMPL", "KMPL"))
        result = doublemetaphone("raspberry")
        self.assertEqual(result, ("RSPR", "RSPR"))

    def test_th_words(self):
        result = doublemetaphone("Thomas")
        self.assertEqual(result, ("TMS", "TMS"))
        result = doublemetaphone("Thames")
        self.assertEqual(result, ("TMS", "TMS"))
