

class std_logic():

    def __init__(self,initialvalue='U'):

        if isinstance(initialvalue,str):
            if len(initialvalue) != 1:
                raise ValueError('length is not 1')

            if ((initialvalue == 'U') or \
                (initialvalue == 'X') or \
                (initialvalue == '0') or \
                (initialvalue == '1') or \
                (initialvalue == 'Z') or \
                (initialvalue == 'W') or \
                (initialvalue == 'L') or \
                (initialvalue == 'H') or \
                (initialvalue == '-')):

                self._value = initialvalue
            else:
                raise ValueError('Unsupported value, only U,X,0,1,Z,W,L,H or - is permitted')

        elif isinstance(initialvalue,int):
            if (initialvalue == 0) or (initialvalue == 1):
                self._value = str(initialvalue)
            else:
                raise ValueError('Unsupported integer value, only 0 or 1 is permitted')
        else:
            raise ValueError('Unsupported type on setup')

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





