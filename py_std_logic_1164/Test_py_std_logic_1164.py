from .std_logic import std_logic
from .std_logic_vector import std_logic_vector

import unittest

class test_std_logic(unittest.TestCase):

    def test_unitialised_create(self):

        temp = std_logic()

        self.assertEqual('%s'%temp,'U')

    def test_int_create(self):

        temp1 = std_logic(1)
        temp0 = std_logic(0)

        self.assertEqual('%s'%temp0,'0')
        self.assertEqual('%s'%temp1,'1')

        with self.assertRaises(ValueError):
            temp = std_logic(2)

    def test_char_create(self):

        legal_values = ['0','1','X','U','Z','W']
        for legal_value in legal_values:
            temp = std_logic(legal_value)
            self.assertEqual('%s'%temp,legal_value)

        with self.assertRaises(ValueError):
            temp = std_logic('z')

            temp = std_logic('ZZ')

            temp = std_logic('00')

    def test_bitwise_and(self):

        # bitwise and
        self.assertEqual(std_logic(0) & std_logic(0),std_logic(0))
        self.assertEqual(std_logic(0) & std_logic(1),std_logic(0))
        self.assertEqual(std_logic(1) & std_logic(0),std_logic(0))
        self.assertEqual(std_logic(1) & std_logic(1),std_logic(1))

        # bitwise or
        self.assertEqual(std_logic(0) | std_logic(0),std_logic(0))
        self.assertEqual(std_logic(0) | std_logic(1),std_logic(1))
        self.assertEqual(std_logic(1) | std_logic(0),std_logic(1))
        self.assertEqual(std_logic(1) | std_logic(1),std_logic(1))

        # bitwise xor
        self.assertEqual(std_logic(0) ^ std_logic(0),std_logic(0))
        self.assertEqual(std_logic(0) ^ std_logic(1),std_logic(1))
        self.assertEqual(std_logic(1) ^ std_logic(0),std_logic(1))
        self.assertEqual(std_logic(1) ^ std_logic(1),std_logic(0))

        # bitwise not
        self.assertEqual(~std_logic(1),std_logic(0))
        self.assertEqual(~std_logic('Z'),std_logic('X'))

    def test_derived_class_operations(self):

        class type1_std_logic(std_logic):
            pass

        class type2_std_logic(std_logic):
            pass

        temp = std_logic(0)
        temp1 = type1_std_logic(0)
        temp2 = type2_std_logic(0)

        self.assertEqual(temp == temp1,True)
        self.assertEqual(temp2 == temp1,True)
        self.assertEqual(temp1 == temp2,True)
        self.assertEqual(temp2 == temp,True)

        self.assertEqual(temp & temp1,std_logic(0))
        self.assertEqual(temp2 & temp1,std_logic(0))
        self.assertEqual(temp1 & temp2,std_logic(0))
        self.assertEqual(temp2 & temp,std_logic(0))

        self.assertEqual(temp | temp1,std_logic(0))
        self.assertEqual(temp2 | temp1,std_logic(0))
        self.assertEqual(temp1 | temp2,std_logic(0))
        self.assertEqual(temp2 | temp,std_logic(0))

        self.assertEqual(temp ^ temp1,std_logic(0))
        self.assertEqual(temp2 ^ temp1,std_logic(0))
        self.assertEqual(temp1 ^ temp2,std_logic(0))
        self.assertEqual(temp2 ^ temp,std_logic(0))

        with self.assertRaises(TypeError):
            self.assertEqual(temp & int(0),std_logic(0))
            self.assertEqual(temp | int(0),std_logic(0))
            self.assertEqual(temp ^ int(0),std_logic(0))


class test_std_logic_vector(unittest.TestCase):

    def test_initialisation(self):
        self.assertEqual('%s'%std_logic_vector('000'),'000')
        self.assertEqual('%s'%std_logic_vector(5),'101')
        self.assertEqual('%s'%std_logic_vector([std_logic(1),std_logic(0)]),'10')

    def test_getting_sections(self):

        temp = std_logic_vector('01Z')

        self.assertEqual(temp[0],std_logic(0))
        self.assertEqual(temp[-1],std_logic('Z'))
        self.assertEqual(temp[1:],std_logic_vector('1Z'))

        with self.assertRaises(IndexError):
            more_temp = temp[3]
            more_temp = temp[-4]

    def test_setting_sections(self):

        temp = std_logic_vector('01Z')

        temp[0] = std_logic(1)
        self.assertEqual(temp,std_logic_vector('11Z'))

        temp[-1] = std_logic(1)
        self.assertEqual(temp,std_logic_vector('111'))

        temp[:2] = std_logic_vector('00')
        self.assertEqual(temp,std_logic_vector('001'))

        temp = std_logic_vector('00000')
        temp[1:4] = std_logic_vector('111')
        self.assertEqual(temp,std_logic_vector('01110'))

    def test_iteration(self):
        temp = ''
        for item in std_logic_vector('10Z'):
            temp += '%s'%item

        self.assertEqual(temp,'10Z')

    def test_printable_forms(self):

        temp = std_logic_vector('10101')

        self.assertEqual('%s'%temp,'10101')
        self.assertEqual('%d'%temp,'21')
        self.assertEqual('%X'%temp,'15')

        self.assertEqual(hex(temp),'0x15')
        self.assertEqual(bin(temp),'0b10101')

    def test_bitwise_operators(self):

        temp1 = std_logic_vector('10101')
        temp2 = std_logic_vector('01101')


        self.assertEqual(~temp1,std_logic_vector('01010'))

        self.assertEqual(temp1 | temp2,std_logic_vector('11101'))
        self.assertEqual(temp1 & temp2,std_logic_vector('00101'))
        self.assertEqual(temp1 ^ temp2,std_logic_vector('11000'))



if __name__ == '__main__':
    unittest.main()



