from .std_logic import std_logic

class std_logic_vector():

    def __init__(self,initialvalue=None):

        self._value = []

        if initialvalue is None:
            self._value = []
        elif isinstance(initialvalue,str):

            for element in initialvalue:
                self._value.append(std_logic(element))

        elif isinstance(initialvalue,int):

            for element in bin(initialvalue)[2:]:
                self._value.append(std_logic(element))

        elif isinstance(initialvalue,list):

            #check every item is a py_std_logic_1164
            for listitem in initialvalue:
                if not isinstance(listitem,std_logic):
                    raise ValueError('only lists of py_std_logic_1164 are permitted')

                self._value.append(listitem)


        else:
            raise(ValueError('Unsupported type on setup'))

    def __int__(self):
        return int(self.__str__(),2)

    def __index__(self):
        return self.__int__()


    def __str__(self):
        return_value = ''
        for element in self._value:
            return_value += '%s'%element

        return return_value

    def __repr__(self):
        base_repr = super().__repr__()
        return base_repr[:-2] + ':%s>'%self

    def __len__(self):
        return len(self._value)

    def __eq__(self, other):

        if isinstance(other,self.__class__):
            return_value = (self._value == other._value)
        else:
            try:
                return_value = (self._value == std_logic_vector(other))
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

        #TODO check the type of other

        if len(other) != len(self):
            raise ValueError('bitwise or can only be perfromed on two std_logic_vectors of the same length')
        else:
            temp = self._value.copy()
            for temp_index in range(len(temp)):
                temp[temp_index] = temp[temp_index] | other[temp_index]

        return std_logic_vector(temp)

    def __and__(self,other):

        #TODO check the type of other

        if len(other) != len(self):
            raise ValueError('bitwise and can only be perfromed on two std_logic_vectors of the same length')
        else:
            temp = self._value.copy()
            for temp_index in range(len(temp)):
                temp[temp_index] = temp[temp_index] & other[temp_index]

        return std_logic_vector(temp)

    def __xor__(self,other):

        #TODO check the type of other

        if len(other) != len(self):
            raise ValueError('bitwise and can only be perfromed on two std_logic_vectors of the same length')
        else:
            temp = self._value.copy()
            for temp_index in range(len(temp)):
                temp[temp_index] = temp[temp_index] ^ other[temp_index]

        return std_logic_vector(temp)

    def reverse(self):
        """
        in place reversal of the bit sequence
        """

        self._value.reverse()

    def append(self,value):
        pass
