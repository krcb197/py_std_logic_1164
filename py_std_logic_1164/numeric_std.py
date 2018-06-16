
import warnings

from .std_logic_vector import std_logic_vector, full, ones
from .std_logic_arithmetic import FullAdderCell
from .std_logic import std_logic

class signed(std_logic_vector):
    pass


class unsigned(std_logic_vector):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self._saturating_overflow = False
        self._saturating_underflow = False
        self._saturating_warnings = True

    @property
    def saturating_overflow(self):
        return self._saturating_overflow

    @property
    def saturating_warnings(self):
        return self._saturating_warnings

    @saturating_overflow.setter
    def saturating_overflow(self,value):
        if isinstance(value,bool):
            self._saturating_overflow = value
        else:
            raise TypeError('saturating_overflow must be set to a boolean value')

    @saturating_warnings.setter
    def saturating_warnings(self,value):
        if isinstance(value,bool):
            self._saturating_warnings = value
        else:
            raise TypeError('saturating_overflow must be set to a boolean value')


    def __add__(self, other):
        return self._add(other=other, inplace=False)

    def __iadd__(self, other):
        return self._add(other=other, inplace=True)

    def _add(self, other, inplace=False):
        """
        internal method for adding together two unsigned values. this method should not be called directly it is usually
        called via the __add__ or __iadd__ class functions

        there are two methods we can used of doing adds
        1) if there are any bits other than 1 or 0 we need to implement this with OR and AND operations, simulating a
           digital adder
        2) if there are only 1 and 0 present the existing methods for adding integers can be used

        this method either operates on itself and returns self (inplace==True) or returns a new object of type unsigned
        (inplace == False)

        :param other: the value to be added to self
        :param inplace: whether the operation on self returns a new object or itself
        :type inplace: bool
        :return:
        """

        if issubclass(other.__class__, unsigned):

            if len(other) != len(self):
                #TODO in a later version we could implement padding to add padding zerso to the other if it shorter than
                #TODO the self

                raise TypeError('length of the two vectors must match')
                return NotImplemented

            else:

                #TODO implement methd 2 however for now we only implement method 1

                return self._rawbit_add(other,inplace=inplace)

        elif isinstance(other,int):

            #TODO implement the method 2 and detection of whether it is possible to use or not.

            # covnert the other to a unsigned and proceed with the maths
            new_other = unsigned(initialvalue=other, bit_length=len(self))
            return self._add(new_other,inplace=inplace)

        else:
            raise TypeError()
            return NotImplemented

    def _rawbit_add(self, other, inplace=False):

        return_value = NotImplemented

        Cbit = std_logic('0')
        if inplace is False:
            return_value = full(len(self),initial_value=std_logic('U'),dtype=unsigned)

            for bit_index in range(0,len(self)):
                (return_value[bit_index],Cbit) = FullAdderCell(self[bit_index],other[bit_index],Cbit)

            if (Cbit == std_logic('1')) and (self.saturating_overflow is True):
                return_value.set_ones()

        elif inplace is True:
            for bit_index in range(0,len(self)):
                (self[bit_index],Cbit) = FullAdderCell(self[bit_index],other[bit_index],Cbit)

            if (Cbit == std_logic('1')) and (self.saturating_overflow is True):
                self.set_ones()

            return_value = self

        if Cbit == std_logic('1'):
            if self.saturating_warnings is True:
                warnings.warn('carry bit is not zero at the end of operation, this may indicate overflow',RuntimeWarning)

        return return_value


    def _numeric_add(self, other):
        return NotImplemented