from .std_logic import std_logic

def full(vector_length,initial_value=std_logic('U')):

    if not isinstance(vector_length,int):
        raise TypeError('vector_length must be of type integer')
    else:
        if vector_length <= 0:
            raise ValueError('vector_length must be more than 0')
        else:
            init_list = []
            for i in range(vector_length):
                init_list.append(initial_value)

            return_item = std_logic_vector(init_list)

    return return_item

def ones(vector_length):
    return full(vector_length=vector_length,initial_value=std_logic('1'))

def zeros(vector_length):
    return full(vector_length=vector_length,initial_value=std_logic('0'))

class std_logic_vector():
    """
    class to represent a digital vector in a similar fashion to the IEEE 1164, std_logic_vector
    """
    def __init__(self,initialvalue=None):
        """
        Initialise the std_logic_vector
        :param initialvalue: used to initialise the std_logic_vector with on creation
        :type NoneType, int, str, list
        """

        self._value = []

        if initialvalue is None:
            self._value = []
        elif isinstance(initialvalue,str):

            for element in initialvalue[::-1]:
                self._value.append(std_logic(element))

        elif isinstance(initialvalue,int):

            for element in bin(initialvalue)[2:]:
                self._value.append(std_logic(element))

        elif isinstance(initialvalue,list):

            #check every item is a py_std_logic_1164
            for listitem in initialvalue:
                if not isinstance(listitem,std_logic):
                    raise TypeError('only lists of py_std_logic_1164 are permitted')

                self._value.append(listitem)


        else:
            raise(TypeError('Unsupported type on setup'))

    def __int__(self):
        if  (std_logic('U') in self._value) or \
            (std_logic('X') in self._value) or \
            (std_logic('W') in self._value) or \
            (std_logic('Z') in self._value) or \
            (std_logic('-') in self._value):
            raise ValueError('unable to convert to integer when std_logic_vector contains U,X,W,Z or -')
        else:
            return int(self.__str__(),2)

    @property
    def value(self):
        """
        returns the internal value of the object as a copy
        :return: list of std_logic
        """
        return self._value.copy()

    def __index__(self):
        return self.__int__()


    def __str__(self):
        return_value = ''
        for element in self._value[::-1]:
            return_value += '%s'%element

        return return_value

    def __repr__(self):
        base_repr = super().__repr__()
        return base_repr[:-2] + ':%s>'%self

    def __len__(self):
        return len(self._value)

    def __eq__(self, other):

        if issubclass(other.__class__,std_logic_vector):
            return_value = (self._value == other._value)
        else:
            try:
                return_value = (self._value == std_logic_vector(other)._value)
            except TypeError:
                return_value = False
            except ValueError:
                return_value = False

        return return_value

    def __getitem__(self, key):

        if isinstance(key,int):
            if key<-len(self):
                raise IndexError('index out of range')
            elif key>=len(self):
                raise IndexError('index out of range')
            else:
                return_value = self._value[key]
        elif isinstance(key,slice):
            return_value = std_logic_vector(self._value[key])
        else:
            raise(IndexError('unable to index into the item'))

        return return_value

    def __setitem__(self,key,value):

        if isinstance(key,int):
            if key<-len(self):
                raise IndexError('index out of range')
            elif key>=len(self):
                raise IndexError('index out of range')
            else:
                if isinstance(value,std_logic):
                    self._value[key] = value
                elif isinstance(value,str):
                    if len(value) != 1:
                        raise ValueError('length of the setting must be 1')
                    else:
                        self._value[key] = std_logic(value)
                elif isinstance(value,int):
                    self._value[key] = std_logic(value)
                else:
                    raise ValueError('must set a single entry to a py_std_logic_1164 vector')
        elif isinstance(key,slice):
            if isinstance(value,std_logic_vector):
                self._value[key] = value
            else:
                raise ValueError('must set a single entry to a py_std_logic_1164 vector')

    def __invert__(self):

        temp = self._value.copy()
        for temp_index in range(len(temp)):
            temp[temp_index] = ~temp[temp_index]

        return std_logic_vector(temp)

    def __or__(self,other):

        if issubclass(other.__class__,std_logic_vector):

            if len(other) != len(self):
                raise ValueError('bitwise or can only be perfromed on two std_logic_vectors of the same length')
            else:
                temp = self._value.copy()
                for temp_index in range(len(temp)):
                    temp[temp_index] = temp[temp_index] | other[temp_index]

            return std_logic_vector(temp)
        else:
            raise TypeError()
            return NotImplemented


    def __and__(self,other):

        if issubclass(other.__class__,std_logic_vector):

            if len(other) != len(self):
                raise ValueError('bitwise and can only be performed on two std_logic_vectors of the same length')
            else:
                temp = self._value.copy()
                for temp_index in range(len(temp)):
                    temp[temp_index] = temp[temp_index] & other[temp_index]

            return std_logic_vector(temp)
        else:
            raise TypeError()
            return NotImplemented

    def __xor__(self,other):

        if issubclass(other.__class__,std_logic_vector):

            if len(other) != len(self):
                raise ValueError('bitwise and can only be perfromed on two std_logic_vectors of the same length')
            else:
                temp = self._value.copy()
                for temp_index in range(len(temp)):
                    temp[temp_index] = temp[temp_index] ^ other[temp_index]

            return std_logic_vector(temp)
        else:
            raise TypeError()
            return NotImplemented

    def __lshift__(self,other):
        pass

    def __rshift__(self,other):
        pass

    def extendMSB(self,number_of_bits,insertion_value=std_logic('U')):
        """
        in place operator to extend the number of bits in the vector, bits are added to the most significant end
        :param number_of_bits: number of bits to extend by
        :type number_of_bits int
        :param insertion_value: std_logic or 1 character string with a valid character that can be converted to a std_logic
        :return:
        """
        if not isinstance(number_of_bits,int):
            raise TypeError('number_of_bits must be an integer')
        else:
            if number_of_bits <= 0:
                raise ValueError('Number of bits to extend by must be greater than zero')
            else:
                for item_count in range(number_of_bits):
                    self._value.append(insertion_value)


    def shortenMSB(self,number_of_bits):
        pass

    def reverse(self):
        """
        in place reversal of the bit sequence
        """

        self._value.reverse()

    def append(self,value):
        pass
