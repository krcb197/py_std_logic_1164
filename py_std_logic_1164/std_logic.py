

class std_logic():
    """
    class to represent a digital bit allowing for the same 9 values of a bit supported by IEEE 1164.
        'U' - Unitialized
        'X' - Unknown
        '0' - Strong 0
        '1' - Strong 1
        'Z' - High Impedance
        'W' - Weak unknown logic
        'L' - Weak logic 0
        'H' - Weak logic 1
        '-' - Don't care

    Refer to https://en.wikipedia.org/wiki/IEEE_1164 for more details
    """
    def __init__(self,initialvalue='U'):
        """
        :param initialvalue: value to be loaded into the bit
        :type initialvalue: int, bool, str
        """
        self._value = 'U'
        self.set(value=initialvalue)

    def __str__(self):

        return self._value

    def __repr__(self):
        base_repr = super().__repr__()
        return base_repr[:-2] + ':%s>'%self._value

    def __eq__(self, other):

        if issubclass(other.__class__,std_logic):
            return self._value == other._value
        else:
            raise NotImplementedError

    def __and__(self,other):

        return_value = NotImplemented

        if issubclass(other.__class__,std_logic):
            """
            truth table from std_logic_1164-body.vhdl
            ----------------------------------------------------
            |  U    X    0    1    Z    W    L    H    -         |   |
            ----------------------------------------------------
            ( 'U', 'U', '0', 'U', 'U', 'U', '0', 'U', 'U' ),  -- | U |
            ( 'U', 'X', '0', 'X', 'X', 'X', '0', 'X', 'X' ),  -- | X |
            ( '0', '0', '0', '0', '0', '0', '0', '0', '0' ),  -- | 0 |
            ( 'U', 'X', '0', '1', 'X', 'X', '0', '1', 'X' ),  -- | 1 |
            ( 'U', 'X', '0', 'X', 'X', 'X', '0', 'X', 'X' ),  -- | Z |
            ( 'U', 'X', '0', 'X', 'X', 'X', '0', 'X', 'X' ),  -- | W |
            ( '0', '0', '0', '0', '0', '0', '0', '0', '0' ),  -- | L |
            ( 'U', 'X', '0', '1', 'X', 'X', '0', '1', 'X' ),  -- | H |
            ( 'U', 'X', '0', 'X', 'X', 'X', '0', 'X', 'X' )   -- | - |
            """

            if self == std_logic('U'):
                if other == std_logic('0') or other == std_logic('L'):
                    return_value = std_logic(0)
                else:
                    return_value = std_logic('U')
            elif self == std_logic('X') or self == std_logic('-') or self == std_logic('W') or self == std_logic('Z'):
                if other == std_logic('U'):
                    return_value = std_logic('U')
                elif other == std_logic('0') or other == std_logic('L'):
                    return_value = std_logic(0)
                else:
                    return_value = std_logic('X')
            elif self == std_logic('0') or self == std_logic('L'):
                return_value = std_logic(0)
            elif self == std_logic('1') or self == std_logic('H'):
                if other == std_logic('U'):
                    return_value = std_logic('U')
                elif other == std_logic('0') or other == std_logic('L'):
                    return_value = std_logic(0)
                elif other == std_logic('1') or other == std_logic('H'):
                    return_value = std_logic(1)
                else:
                    return_value = std_logic('X')
        else:
            raise TypeError('can not perform operation on classes')


        return return_value

    def __xor__(self, other):
        """
        perfroms a bitwise xor operation
        :param other:
        :return: self ^ other
        """

        return_value = NotImplemented

        if issubclass(other.__class__,std_logic):
            """
            truth table from std_logic_1164-body.vhdl
            ----------------------------------------------------
            |  U    X    0    1    Z    W    L    H    -         |   |  
            ----------------------------------------------------
             ('U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),  -- | U |
             ('U', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'),  -- | X |
             ('U', 'X', '0', '1', 'X', 'X', '0', '1', 'X'),  -- | 0 |
             ('U', 'X', '1', '0', 'X', 'X', '1', '0', 'X'),  -- | 1 |
             ('U', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'),  -- | Z |
             ('U', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'),  -- | W |
             ('U', 'X', '0', '1', 'X', 'X', '0', '1', 'X'),  -- | L |
             ('U', 'X', '1', '0', 'X', 'X', '1', '0', 'X'),  -- | H |
             ('U', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X')   -- | - |
             );
            """

            if self == std_logic('U'):
                return_value = std_logic('U')
            elif self == std_logic('X') or self == std_logic('-') or self == std_logic('W') or self == std_logic('Z'):
                if other == std_logic('U'):
                    return_value = std_logic('U')
                else:
                    return_value = std_logic('X')
            elif self == std_logic('1') or self == std_logic('H'):
                if other == std_logic('U'):
                    return_value = std_logic('U')
                elif other == std_logic('0') or other == std_logic('L'):
                    return_value = std_logic(1)
                elif other == std_logic('1') or other == std_logic('H'):
                    return_value = std_logic(0)
                else:
                    return_value = std_logic('X')
            elif self == std_logic('0') or self == std_logic('L'):
                if other == std_logic('U'):
                    return_value = std_logic('U')
                elif other == std_logic('0') or other == std_logic('L'):
                    return_value = std_logic(0)
                elif other == std_logic('1') or other == std_logic('H'):
                    return_value = std_logic(1)
                else:
                    return_value = std_logic('X')
        else:
            raise TypeError('can not perform operation on classes')

        return return_value

    def __or__(self,other):


        return_value = NotImplemented

        if issubclass(other.__class__,std_logic):
            """
            truth table from std_logic_1164-body.vhdl
    
            ----------------------------------------------------
            |  U    X    0    1    Z    W    L    H    -         |   |
            ----------------------------------------------------
             ('U', 'U', 'U', '1', 'U', 'U', 'U', '1', 'U'),  -- | U |
             ('U', 'X', 'X', '1', 'X', 'X', 'X', '1', 'X'),  -- | X |
             ('U', 'X', '0', '1', 'X', 'X', '0', '1', 'X'),  -- | 0 |
             ('1', '1', '1', '1', '1', '1', '1', '1', '1'),  -- | 1 |
             ('U', 'X', 'X', '1', 'X', 'X', 'X', '1', 'X'),  -- | Z |
             ('U', 'X', 'X', '1', 'X', 'X', 'X', '1', 'X'),  -- | W |
             ('U', 'X', '0', '1', 'X', 'X', '0', '1', 'X'),  -- | L |
             ('1', '1', '1', '1', '1', '1', '1', '1', '1'),  -- | H |
             ('U', 'X', 'X', '1', 'X', 'X', 'X', '1', 'X')   -- | - |
             )
            """

            if self == std_logic('U'):
                if other == std_logic('1') or other == std_logic('H'):
                    return_value = std_logic(1)
                else:
                    return_value = std_logic('U')
            elif self == std_logic('X') or self == std_logic('-') or self == std_logic('W') or self == std_logic('Z'):
                if other == std_logic('U'):
                    return_value = std_logic('U')
                elif other == std_logic('1') or other == std_logic('H'):
                    return_value = std_logic(1)
                else:
                    return_value = std_logic('X')
            elif self == std_logic('1') or self == std_logic('H'):
                return_value = std_logic(1)
            elif self == std_logic('0') or self == std_logic('L'):
                if other == std_logic('U'):
                    return_value = std_logic('U')
                elif other == std_logic('0') or other == std_logic('L'):
                    return_value = std_logic(0)
                elif other == std_logic('1') or other == std_logic('H'):
                    return_value = std_logic(1)
                else:
                    return_value = std_logic('X')
        else:
            raise TypeError('can not perform operation on classes')


        return return_value

    def __invert__(self):

        """
        truth table from std_logic_1164-body.vhdl
        -------------------------------------------------
        |   U    X    0    1    Z    W    L    H    -   |
        -------------------------------------------------
          ('U', 'X', '1', '0', 'X', 'X', '1', '0', 'X')

        """

        if self == std_logic('U'):
            return_value = std_logic('U')
        elif self == std_logic('X') or self == std_logic('-') or self == std_logic('W') or self == std_logic('Z'):
            return_value = std_logic('X')
        elif self == std_logic('0') or self == std_logic('L'):
            return_value = std_logic(1)
        elif self == std_logic('1') or self == std_logic('H'):
            return_value = std_logic(0)

        return return_value

    def set(self,value):
        """
        in place value set
        :param value: value to be loaded into the bit
        :type value: int, bool, str
        """
        if isinstance(value,str):
            if len(value) != 1:
                raise ValueError('length is not 1')

            if ((value == 'U') or
                    (value == 'X') or
                    (value == '0') or
                    (value == '1') or
                    (value == 'Z') or
                    (value == 'W') or
                    (value == 'L') or
                    (value == 'H') or
                    (value == '-')):

                self._value = value
            else:
                raise ValueError('Unsupported value, only U,X,0,1,Z,W,L,H or - is permitted')

        elif isinstance(value,bool):
            if value is False:
                self._value = '0'
            elif value is True:
                self._value = '1'
            else:
                raise ValueError('Illegal boolean value')

        elif isinstance(value,int):
            if (value == 0) or (value == 1):
                self._value = str(value)
                assert (self._value == '1') or (self._value == '0')
            else:
                raise ValueError('Unsupported integer value, only 0 or 1 is permitted')
        else:
            raise ValueError('Unsupported type')





