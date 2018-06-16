from .std_logic import std_logic
from .std_logic_vector import std_logic_vector,full,ones,zeros
from .numeric_std import signed,unsigned

import unittest

class test_std_logic(unittest.TestCase):
    """
    Tests for the std_logic class
    """

    def test_unitialised_create(self):
        """
        Check that the unitialized value of the object is 'U'
        :return:
        """

        temp = std_logic()

        self.assertEqual('%s'%temp, 'U')

    def test_int_create(self):

        self.assertEqual('%s'%std_logic(0),'0')
        self.assertEqual('%s'%std_logic(1),'1')

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

    def test_boolean_create(self):

        self.assertEqual('%s'%std_logic(False),'0')
        self.assertEqual('%s'%std_logic(True),'1')

    def test_bitwise_and(self):

        # bitwise and
        self.assertEqual(std_logic(0) & std_logic(0), std_logic(0))
        self.assertEqual(std_logic(0) & std_logic(1), std_logic(0))
        self.assertEqual(std_logic(1) & std_logic(0), std_logic(0))
        self.assertEqual(std_logic(1) & std_logic(1), std_logic(1))

        # bitwise or
        self.assertEqual(std_logic(0) | std_logic(0), std_logic(0))
        self.assertEqual(std_logic(0) | std_logic(1), std_logic(1))
        self.assertEqual(std_logic(1) | std_logic(0), std_logic(1))
        self.assertEqual(std_logic(1) | std_logic(1), std_logic(1))

        # bitwise xor
        self.assertEqual(std_logic(0) ^ std_logic(0), std_logic(0))
        self.assertEqual(std_logic(0) ^ std_logic(1), std_logic(1))
        self.assertEqual(std_logic(1) ^ std_logic(0), std_logic(1))
        self.assertEqual(std_logic(1) ^ std_logic(1), std_logic(0))

        # bitwise not
        self.assertEqual(~std_logic(1), std_logic(0))
        self.assertEqual(~std_logic('Z'), std_logic('X'))

    def test_derived_class_operations(self):

        class type1_std_logic(std_logic):
            pass

        class type2_std_logic(std_logic):
            pass

        temp = std_logic(0)
        temp1 = type1_std_logic(0)
        temp2 = type2_std_logic(0)

        self.assertEqual(temp == temp1, True)
        self.assertEqual(temp2 == temp1, True)
        self.assertEqual(temp1 == temp2, True)
        self.assertEqual(temp2 == temp, True)

        self.assertEqual(temp & temp1, std_logic(0))
        self.assertEqual(temp2 & temp1, std_logic(0))
        self.assertEqual(temp1 & temp2, std_logic(0))
        self.assertEqual(temp2 & temp, std_logic(0))

        self.assertEqual(temp | temp1, std_logic(0))
        self.assertEqual(temp2 | temp1, std_logic(0))
        self.assertEqual(temp1 | temp2, std_logic(0))
        self.assertEqual(temp2 | temp, std_logic(0))

        self.assertEqual(temp ^ temp1, std_logic(0))
        self.assertEqual(temp2 ^ temp1, std_logic(0))
        self.assertEqual(temp1 ^ temp2, std_logic(0))
        self.assertEqual(temp2 ^ temp, std_logic(0))

        with self.assertRaises(TypeError):
            self.assertEqual(temp & int(0), std_logic(0))
            self.assertEqual(temp | int(0), std_logic(0))
            self.assertEqual(temp ^ int(0), std_logic(0))


class test_std_logic_vector(unittest.TestCase):

    def test_initialisation(self):

        temp = []
        temp = [None,None]
        temp[0] = std_logic('0')
        temp[1] = std_logic('1')

        self.assertEqual('%s'%std_logic_vector('000'), '000')
        self.assertEqual('%s'%std_logic_vector(5), '101')
        self.assertEqual('%s'%std_logic_vector(temp), '10')

        with self.assertRaises(TypeError):
            a = std_logic_vector(5.0)

        with self.assertRaises(ValueError):
            a = std_logic_vector('1J0')

    def test_getting_sections(self):

        temp = std_logic_vector('01Z')

        self.assertEqual(temp[0], std_logic('Z'))
        self.assertEqual(temp[-1], std_logic('0'))
        self.assertEqual(temp[1:], std_logic_vector('01'))

        with self.assertRaises(IndexError):
            more_temp = temp[3]

        with self.assertRaises(IndexError):
            more_temp = temp[-4]

    def test_setting_sections(self):

        temp = std_logic_vector('01Z')

        temp[0] = std_logic(1)
        self.assertEqual(temp, std_logic_vector('011'))

        temp[-1] = std_logic(1)
        self.assertEqual(temp, std_logic_vector('111'))

        temp[:2] = std_logic_vector('00')
        self.assertEqual(temp, std_logic_vector('100'))

        temp = std_logic_vector('00000')
        temp[1:4] = std_logic_vector('U11')
        self.assertEqual(temp,std_logic_vector('0U110'))

    def test_iteration(self):
        temp = ''
        for item in std_logic_vector('10Z'):
            temp += '%s'%item

        self.assertEqual(temp,'Z01')

    def test_printable_forms(self):

        temp = std_logic_vector('10101')

        self.assertEqual('%s'%temp, '10101')
        self.assertEqual('%d'%temp, '21')
        self.assertEqual('%X'%temp, '15')

        self.assertEqual(hex(temp), '0x15')
        self.assertEqual(bin(temp), '0b10101')

        with self.assertRaises(ValueError):
            temp_report = '%d'%std_logic_vector('1Z0')

    def test_bitwise_operators(self):

        temp1 = std_logic_vector('10101')
        temp2 = std_logic_vector('01101')


        self.assertEqual(~temp1,std_logic_vector('01010'))

        self.assertEqual(temp1 | temp2, std_logic_vector('11101'))
        self.assertEqual(temp1 & temp2, std_logic_vector('00101'))
        self.assertEqual(temp1 ^ temp2, std_logic_vector('11000'))

    def test_numeric_operators_unimplemented(self):
        """
        The std_logic_vector should not implement any of the following, instead the classes in
        :return:
        """
        a = std_logic_vector('101')
        b = std_logic_vector('001')
        with self.assertRaises(TypeError):
            c = a + b

        with self.assertRaises(TypeError):
            c = a - b

        with self.assertRaises(TypeError):
            c = a / b

        with self.assertRaises(TypeError):
            c = a * b

    def test_derived_classes(self):
        class type1_std_logic_vector(std_logic_vector):
            pass

        class type2_std_logic_vector(std_logic_vector):
            pass

        temp = std_logic_vector('01')
        temp1 = type1_std_logic_vector('01')
        temp2 = type2_std_logic_vector('01')

        self.assertEqual(temp == temp1, True)
        self.assertEqual(temp2 == temp1, True)
        self.assertEqual(temp1 == temp2, True)
        self.assertEqual(temp2 == temp, True)

        self.assertEqual(temp & temp1, temp)
        self.assertEqual(temp2 & temp1, temp)
        self.assertEqual(temp1 & temp2, temp)
        self.assertEqual(temp2 & temp, temp)

        self.assertEqual(temp | temp1, temp)
        self.assertEqual(temp2 | temp1, temp)
        self.assertEqual(temp1 | temp2, temp)
        self.assertEqual(temp2 | temp, temp)

        self.assertEqual(temp ^ temp1, std_logic_vector('00'))
        self.assertEqual(temp2 ^ temp1, std_logic_vector('00'))
        self.assertEqual(temp1 ^ temp2, std_logic_vector('00'))
        self.assertEqual(temp2 ^ temp, std_logic_vector('00'))

        with self.assertRaises(TypeError):
            self.assertEqual(temp & int(0), temp)
        with self.assertRaises(TypeError):
            self.assertEqual(temp | int(0), temp)
        with self.assertRaises(TypeError):
            self.assertEqual(temp ^ int(0), temp)

        self.assertEqual(temp == int(0), False)

    def test_initialisation_methods(self):
        self.assertEqual(full(10,std_logic('Z')), std_logic_vector('ZZZZZZZZZZ'))
        self.assertEqual(ones(4), std_logic_vector('1111'))
        self.assertEqual(zeros(3), std_logic_vector('000'))

class test_numeric_std(unittest.TestCase):

    def test_adding_operations(self):

        a = unsigned(4,bit_length=3)
        b = unsigned(3,bit_length=3)

        self.assertEqual( (a + b).__int__(), 7)

        # because the length of the vector is 3 then it should roll over and return 0, it will generate a runtime warning
        with self.assertWarns(RuntimeWarning):
            result = a + a
        self.assertEqual( result.__int__(), 0)

        # next we turn on addition saturation,
        a.saturating_overflow = True
        with self.assertWarns(RuntimeWarning):
            result = a + a
        self.assertEqual( result , ones(len(a), dtype=unsigned))

        a.saturating_warnings = False
        result = a + a
        self.assertEqual( result , ones(len(a), dtype=unsigned))

        result = a + 2
        self.assertEqual(result.__int__(), 6)
        self.assertEqual(a.__int__(), 4)


        a += 2
        self.assertEqual(a.__int__(), 6)


if __name__ == '__main__':
    unittest.main()



