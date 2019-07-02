from enum import IntFlag, IntEnum, Enum, auto


class IntEnumRepr(IntEnum):
    def __repr__(self):
        return "{}.{}".format(self.__class__.__name__, self.name)


class ConfigByte(IntFlag):
    ECR_PRINTS_PAYMENT = 0x02
    ECR_PRINTS_ADMIN = 0x04
    ECR_INTERMEDIATE_STATUS = 0x08
    ECR_CONTROLS_PAYMENT = 0x10
    ECR_CONTROLS_ADMIN = 0x20
    ECR_USE_PRINT_LINES = 0x80

    ALL_BUT_ADMIN_RECEIPT = DEFAULT = 0xba
    ALL = 0xbe


class ServiceByte(IntFlag):
    SERVICE_MENU_NOT_ASSIGNED = 0x01
    USE_CAPITALS = 0x02

    NONE = DEFAULT = 0x00


class CurrencyCode(IntEnumRepr):
    EUR = 978


class CharacterSet(IntEnum):
    ASCII_7BIT = 0
    ISO_8859_1 = LATIN_1 = 1
    ISO_8859_2 = LATIN_2 = 2
    ISO_8859_3 = LATIN_3 = 3
    ISO_8859_4 = LATIN_4 = 4
    ISO_8859_5 = LATIN_5 = 5
    ISO_8859_6 = LATIN_6 = 6
    ISO_8859_7 = LATIN_7 = 7
    ISO_8859_8 = LATIN_8 = 8
    ISO_8859_9 = LATIN_9 = 9
    ISO_8859_10 = LATIN_10 = 10
    ISO_8859_11 = LATIN_11 = 11
    # ISO 8859-12 is not specified
    ISO_8859_13 = LATIN_13 = 13
    ISO_8859_14 = LATIN_14 = 14
    ISO_8859_15 = LATIN_15 = 15
    ISO_8859_16 = LATIN_16 = 16
    UTF8 = 0xfe
    ZVT_8BIT = CP437 = DEFAULT = 0xff


class VendorQuirks(Enum):
    FEIG_CVEND = auto()
