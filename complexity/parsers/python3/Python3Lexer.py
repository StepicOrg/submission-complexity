# Generated from complexity/grammars/Python3.g4 by ANTLR 4.7
import importlib
import re
import sys
from io import StringIO

from antlr4 import *
from antlr4.Token import CommonToken
from typing.io import TextIO

# Allow languages to extend the lexer and parser, by loading the parser dinamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2]")
        buf.write("\u0347\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u01a5\n#\3#\3#\5#\u01a9")
        buf.write("\n#\3#\5#\u01ac\n#\5#\u01ae\n#\3#\3#\3$\3$\7$\u01b4\n")
        buf.write("$\f$\16$\u01b7\13$\3%\5%\u01ba\n%\3%\5%\u01bd\n%\3%\3")
        buf.write("%\5%\u01c1\n%\3%\3%\5%\u01c5\n%\3%\3%\5%\u01c9\n%\5%\u01cb")
        buf.write("\n%\3&\3&\7&\u01cf\n&\f&\16&\u01d2\13&\3&\6&\u01d5\n&")
        buf.write("\r&\16&\u01d6\5&\u01d9\n&\3\'\3\'\3\'\6\'\u01de\n\'\r")
        buf.write("\'\16\'\u01df\3(\3(\3(\6(\u01e5\n(\r(\16(\u01e6\3)\3)")
        buf.write("\3)\6)\u01ec\n)\r)\16)\u01ed\3*\3*\5*\u01f2\n*\3+\3+\5")
        buf.write("+\u01f6\n+\3+\3+\3,\3,\3-\3-\3-\3-\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3F\3F\3G\3G\3G\3H\3H\3")
        buf.write("H\3I\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3M\3M\3M\3N\3N\3N\3")
        buf.write("O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3T\3T\3T\3")
        buf.write("U\3U\3U\3V\3V\3V\3W\3W\3W\3W\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3")
        buf.write("Z\3Z\3Z\3Z\3[\3[\3[\5[\u027e\n[\3[\3[\3\\\3\\\3]\3]\3")
        buf.write("]\7]\u0287\n]\f]\16]\u028a\13]\3]\3]\3]\3]\7]\u0290\n")
        buf.write("]\f]\16]\u0293\13]\3]\5]\u0296\n]\3^\3^\3^\3^\3^\7^\u029d")
        buf.write("\n^\f^\16^\u02a0\13^\3^\3^\3^\3^\3^\3^\3^\3^\7^\u02aa")
        buf.write("\n^\f^\16^\u02ad\13^\3^\3^\3^\5^\u02b2\n^\3_\3_\5_\u02b6")
        buf.write("\n_\3`\3`\3a\3a\3a\3b\3b\3c\3c\3d\3d\3e\3e\3f\3f\3g\5")
        buf.write("g\u02c8\ng\3g\3g\3g\3g\5g\u02ce\ng\3h\3h\5h\u02d2\nh\3")
        buf.write("h\3h\3i\6i\u02d7\ni\ri\16i\u02d8\3j\3j\6j\u02dd\nj\rj")
        buf.write("\16j\u02de\3k\3k\5k\u02e3\nk\3k\6k\u02e6\nk\rk\16k\u02e7")
        buf.write("\3l\3l\3l\7l\u02ed\nl\fl\16l\u02f0\13l\3l\3l\3l\3l\7l")
        buf.write("\u02f6\nl\fl\16l\u02f9\13l\3l\5l\u02fc\nl\3m\3m\3m\3m")
        buf.write("\3m\7m\u0303\nm\fm\16m\u0306\13m\3m\3m\3m\3m\3m\3m\3m")
        buf.write("\3m\7m\u0310\nm\fm\16m\u0313\13m\3m\3m\3m\5m\u0318\nm")
        buf.write("\3n\3n\5n\u031c\nn\3o\5o\u031f\no\3p\5p\u0322\np\3q\5")
        buf.write("q\u0325\nq\3r\3r\3r\3s\6s\u032b\ns\rs\16s\u032c\3t\3t")
        buf.write("\7t\u0331\nt\ft\16t\u0334\13t\3u\3u\5u\u0338\nu\3u\5u")
        buf.write("\u033b\nu\3u\3u\5u\u033f\nu\3v\5v\u0342\nv\3w\3w\5w\u0346")
        buf.write("\nw\6\u029e\u02ab\u0304\u0311\2x\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1")
        buf.write("R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00adX\u00afY\u00b1")
        buf.write("Z\u00b3[\u00b5\\\u00b7]\u00b9\2\u00bb\2\u00bd\2\u00bf")
        buf.write("\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd")
        buf.write("\2\u00cf\2\u00d1\2\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db")
        buf.write("\2\u00dd\2\u00df\2\u00e1\2\u00e3\2\u00e5\2\u00e7\2\u00e9")
        buf.write("\2\u00eb\2\u00ed\2\3\2\32\4\2WWww\4\2TTtt\4\2DDdd\4\2")
        buf.write("QQqq\4\2ZZzz\4\2LLll\6\2\f\f\17\17))^^\6\2\f\f\17\17$")
        buf.write("$^^\3\2^^\3\2\63;\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63")
        buf.write("\4\2GGgg\4\2--//\7\2\2\13\r\16\20(*]_\u0081\7\2\2\13\r")
        buf.write("\16\20#%]_\u0081\4\2\2]_\u0081\3\2\2\u0081\4\2\13\13\"")
        buf.write("\"\4\2\f\f\17\17\u0129\2C\\aac|\u00ac\u00ac\u00b7\u00b7")
        buf.write("\u00bc\u00bc\u00c2\u00d8\u00da\u00f8\u00fa\u0243\u0252")
        buf.write("\u02c3\u02c8\u02d3\u02e2\u02e6\u02f0\u02f0\u037c\u037c")
        buf.write("\u0388\u0388\u038a\u038c\u038e\u038e\u0390\u03a3\u03a5")
        buf.write("\u03d0\u03d2\u03f7\u03f9\u0483\u048c\u04d0\u04d2\u04fb")
        buf.write("\u0502\u0511\u0533\u0558\u055b\u055b\u0563\u0589\u05d2")
        buf.write("\u05ec\u05f2\u05f4\u0623\u063c\u0642\u064c\u0670\u0671")
        buf.write("\u0673\u06d5\u06d7\u06d7\u06e7\u06e8\u06f0\u06f1\u06fc")
        buf.write("\u06fe\u0701\u0701\u0712\u0712\u0714\u0731\u074f\u076f")
        buf.write("\u0782\u07a7\u07b3\u07b3\u0906\u093b\u093f\u093f\u0952")
        buf.write("\u0952\u095a\u0963\u097f\u097f\u0987\u098e\u0991\u0992")
        buf.write("\u0995\u09aa\u09ac\u09b2\u09b4\u09b4\u09b8\u09bb\u09bf")
        buf.write("\u09bf\u09d0\u09d0\u09de\u09df\u09e1\u09e3\u09f2\u09f3")
        buf.write("\u0a07\u0a0c\u0a11\u0a12\u0a15\u0a2a\u0a2c\u0a32\u0a34")
        buf.write("\u0a35\u0a37\u0a38\u0a3a\u0a3b\u0a5b\u0a5e\u0a60\u0a60")
        buf.write("\u0a74\u0a76\u0a87\u0a8f\u0a91\u0a93\u0a95\u0aaa\u0aac")
        buf.write("\u0ab2\u0ab4\u0ab5\u0ab7\u0abb\u0abf\u0abf\u0ad2\u0ad2")
        buf.write("\u0ae2\u0ae3\u0b07\u0b0e\u0b11\u0b12\u0b15\u0b2a\u0b2c")
        buf.write("\u0b32\u0b34\u0b35\u0b37\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f")
        buf.write("\u0b61\u0b63\u0b73\u0b73\u0b85\u0b85\u0b87\u0b8c\u0b90")
        buf.write("\u0b92\u0b94\u0b97\u0b9b\u0b9c\u0b9e\u0b9e\u0ba0\u0ba1")
        buf.write("\u0ba5\u0ba6\u0baa\u0bac\u0bb0\u0bbb\u0c07\u0c0e\u0c10")
        buf.write("\u0c12\u0c14\u0c2a\u0c2c\u0c35\u0c37\u0c3b\u0c62\u0c63")
        buf.write("\u0c87\u0c8e\u0c90\u0c92\u0c94\u0caa\u0cac\u0cb5\u0cb7")
        buf.write("\u0cbb\u0cbf\u0cbf\u0ce0\u0ce0\u0ce2\u0ce3\u0d07\u0d0e")
        buf.write("\u0d10\u0d12\u0d14\u0d2a\u0d2c\u0d3b\u0d62\u0d63\u0d87")
        buf.write("\u0d98\u0d9c\u0db3\u0db5\u0dbd\u0dbf\u0dbf\u0dc2\u0dc8")
        buf.write("\u0e03\u0e32\u0e34\u0e35\u0e42\u0e48\u0e83\u0e84\u0e86")
        buf.write("\u0e86\u0e89\u0e8a\u0e8c\u0e8c\u0e8f\u0e8f\u0e96\u0e99")
        buf.write("\u0e9b\u0ea1\u0ea3\u0ea5\u0ea7\u0ea7\u0ea9\u0ea9\u0eac")
        buf.write("\u0ead\u0eaf\u0eb2\u0eb4\u0eb5\u0ebf\u0ebf\u0ec2\u0ec6")
        buf.write("\u0ec8\u0ec8\u0ede\u0edf\u0f02\u0f02\u0f42\u0f49\u0f4b")
        buf.write("\u0f6c\u0f8a\u0f8d\u1002\u1023\u1025\u1029\u102b\u102c")
        buf.write("\u1052\u1057\u10a2\u10c7\u10d2\u10fc\u10fe\u10fe\u1102")
        buf.write("\u115b\u1161\u11a4\u11aa\u11fb\u1202\u124a\u124c\u124f")
        buf.write("\u1252\u1258\u125a\u125a\u125c\u125f\u1262\u128a\u128c")
        buf.write("\u128f\u1292\u12b2\u12b4\u12b7\u12ba\u12c0\u12c2\u12c2")
        buf.write("\u12c4\u12c7\u12ca\u12d8\u12da\u1312\u1314\u1317\u131a")
        buf.write("\u135c\u1382\u1391\u13a2\u13f6\u1403\u166e\u1671\u1678")
        buf.write("\u1683\u169c\u16a2\u16ec\u16f0\u16f2\u1702\u170e\u1710")
        buf.write("\u1713\u1722\u1733\u1742\u1753\u1762\u176e\u1770\u1772")
        buf.write("\u1782\u17b5\u17d9\u17d9\u17de\u17de\u1822\u1879\u1882")
        buf.write("\u18aa\u1902\u191e\u1952\u196f\u1972\u1976\u1982\u19ab")
        buf.write("\u19c3\u19c9\u1a02\u1a18\u1d02\u1dc1\u1e02\u1e9d\u1ea2")
        buf.write("\u1efb\u1f02\u1f17\u1f1a\u1f1f\u1f22\u1f47\u1f4a\u1f4f")
        buf.write("\u1f52\u1f59\u1f5b\u1f5b\u1f5d\u1f5d\u1f5f\u1f5f\u1f61")
        buf.write("\u1f7f\u1f82\u1fb6\u1fb8\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6")
        buf.write("\u1fc8\u1fce\u1fd2\u1fd5\u1fd8\u1fdd\u1fe2\u1fee\u1ff4")
        buf.write("\u1ff6\u1ff8\u1ffe\u2073\u2073\u2081\u2081\u2092\u2096")
        buf.write("\u2104\u2104\u2109\u2109\u210c\u2115\u2117\u2117\u211a")
        buf.write("\u211f\u2126\u2126\u2128\u2128\u212a\u212a\u212c\u2133")
        buf.write("\u2135\u213b\u213e\u2141\u2147\u214b\u2162\u2185\u2c02")
        buf.write("\u2c30\u2c32\u2c60\u2c82\u2ce6\u2d02\u2d27\u2d32\u2d67")
        buf.write("\u2d71\u2d71\u2d82\u2d98\u2da2\u2da8\u2daa\u2db0\u2db2")
        buf.write("\u2db8\u2dba\u2dc0\u2dc2\u2dc8\u2dca\u2dd0\u2dd2\u2dd8")
        buf.write("\u2dda\u2de0\u3007\u3009\u3023\u302b\u3033\u3037\u303a")
        buf.write("\u303e\u3043\u3098\u309d\u30a1\u30a3\u30fc\u30fe\u3101")
        buf.write("\u3107\u312e\u3133\u3190\u31a2\u31b9\u31f2\u3201\u3402")
        buf.write("\u4db7\u4e02\u9fbd\ua002\ua48e\ua802\ua803\ua805\ua807")
        buf.write("\ua809\ua80c\ua80e\ua824\uac02\ud7a5\uf902\ufa2f\ufa32")
        buf.write("\ufa6c\ufa72\ufadb\ufb02\ufb08\ufb15\ufb19\ufb1f\ufb1f")
        buf.write("\ufb21\ufb2a\ufb2c\ufb38\ufb3a\ufb3e\ufb40\ufb40\ufb42")
        buf.write("\ufb43\ufb45\ufb46\ufb48\ufbb3\ufbd5\ufd3f\ufd52\ufd91")
        buf.write("\ufd94\ufdc9\ufdf2\ufdfd\ufe72\ufe76\ufe78\ufefe\uff23")
        buf.write("\uff3c\uff43\uff5c\uff68\uffc0\uffc4\uffc9\uffcc\uffd1")
        buf.write("\uffd4\uffd9\uffdc\uffde\u0096\2\62;\u0302\u0371\u0485")
        buf.write("\u0488\u0593\u05bb\u05bd\u05bf\u05c1\u05c1\u05c3\u05c4")
        buf.write("\u05c6\u05c7\u05c9\u05c9\u0612\u0617\u064d\u0660\u0662")
        buf.write("\u066b\u0672\u0672\u06d8\u06de\u06e1\u06e6\u06e9\u06ea")
        buf.write("\u06ec\u06ef\u06f2\u06fb\u0713\u0713\u0732\u074c\u07a8")
        buf.write("\u07b2\u0903\u0905\u093e\u093e\u0940\u094f\u0953\u0956")
        buf.write("\u0964\u0965\u0968\u0971\u0983\u0985\u09be\u09be\u09c0")
        buf.write("\u09c6\u09c9\u09ca\u09cd\u09cf\u09d9\u09d9\u09e4\u09e5")
        buf.write("\u09e8\u09f1\u0a03\u0a05\u0a3e\u0a3e\u0a40\u0a44\u0a49")
        buf.write("\u0a4a\u0a4d\u0a4f\u0a68\u0a73\u0a83\u0a85\u0abe\u0abe")
        buf.write("\u0ac0\u0ac7\u0ac9\u0acb\u0acd\u0acf\u0ae4\u0ae5\u0ae8")
        buf.write("\u0af1\u0b03\u0b05\u0b3e\u0b3e\u0b40\u0b45\u0b49\u0b4a")
        buf.write("\u0b4d\u0b4f\u0b58\u0b59\u0b68\u0b71\u0b84\u0b84\u0bc0")
        buf.write("\u0bc4\u0bc8\u0bca\u0bcc\u0bcf\u0bd9\u0bd9\u0be8\u0bf1")
        buf.write("\u0c03\u0c05\u0c40\u0c46\u0c48\u0c4a\u0c4c\u0c4f\u0c57")
        buf.write("\u0c58\u0c68\u0c71\u0c84\u0c85\u0cbe\u0cbe\u0cc0\u0cc6")
        buf.write("\u0cc8\u0cca\u0ccc\u0ccf\u0cd7\u0cd8\u0ce8\u0cf1\u0d04")
        buf.write("\u0d05\u0d40\u0d45\u0d48\u0d4a\u0d4c\u0d4f\u0d59\u0d59")
        buf.write("\u0d68\u0d71\u0d84\u0d85\u0dcc\u0dcc\u0dd1\u0dd6\u0dd8")
        buf.write("\u0dd8\u0dda\u0de1\u0df4\u0df5\u0e33\u0e33\u0e36\u0e3c")
        buf.write("\u0e49\u0e50\u0e52\u0e5b\u0eb3\u0eb3\u0eb6\u0ebb\u0ebd")
        buf.write("\u0ebe\u0eca\u0ecf\u0ed2\u0edb\u0f1a\u0f1b\u0f22\u0f2b")
        buf.write("\u0f37\u0f37\u0f39\u0f39\u0f3b\u0f3b\u0f40\u0f41\u0f73")
        buf.write("\u0f86\u0f88\u0f89\u0f92\u0f99\u0f9b\u0fbe\u0fc8\u0fc8")
        buf.write("\u102e\u1034\u1038\u103b\u1042\u104b\u1058\u105b\u1361")
        buf.write("\u1361\u136b\u1373\u1714\u1716\u1734\u1736\u1754\u1755")
        buf.write("\u1774\u1775\u17b8\u17d5\u17df\u17df\u17e2\u17eb\u180d")
        buf.write("\u180f\u1812\u181b\u18ab\u18ab\u1922\u192d\u1932\u193d")
        buf.write("\u1948\u1951\u19b2\u19c2\u19ca\u19cb\u19d2\u19db\u1a19")
        buf.write("\u1a1d\u1dc2\u1dc5\u2041\u2042\u2056\u2056\u20d2\u20de")
        buf.write("\u20e3\u20e3\u20e7\u20ed\u302c\u3031\u309b\u309c\ua804")
        buf.write("\ua804\ua808\ua808\ua80d\ua80d\ua825\ua829\ufb20\ufb20")
        buf.write("\ufe02\ufe11\ufe22\ufe25\ufe35\ufe36\ufe4f\ufe51\uff12")
        buf.write("\uff1b\uff41\uff41\2\u035f\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\3\u00ef\3\2\2\2\5\u00f3\3\2\2\2\7\u00fa\3\2\2")
        buf.write("\2\t\u0100\3\2\2\2\13\u0105\3\2\2\2\r\u010c\3\2\2\2\17")
        buf.write("\u010f\3\2\2\2\21\u0116\3\2\2\2\23\u011f\3\2\2\2\25\u0126")
        buf.write("\3\2\2\2\27\u0129\3\2\2\2\31\u012e\3\2\2\2\33\u0133\3")
        buf.write("\2\2\2\35\u0139\3\2\2\2\37\u013d\3\2\2\2!\u0140\3\2\2")
        buf.write("\2#\u0144\3\2\2\2%\u014c\3\2\2\2\'\u0151\3\2\2\2)\u0158")
        buf.write("\3\2\2\2+\u015f\3\2\2\2-\u0162\3\2\2\2/\u0166\3\2\2\2")
        buf.write("\61\u016a\3\2\2\2\63\u016d\3\2\2\2\65\u0172\3\2\2\2\67")
        buf.write("\u0177\3\2\2\29\u017d\3\2\2\2;\u0183\3\2\2\2=\u0189\3")
        buf.write("\2\2\2?\u018d\3\2\2\2A\u0192\3\2\2\2C\u019b\3\2\2\2E\u01ad")
        buf.write("\3\2\2\2G\u01b1\3\2\2\2I\u01ca\3\2\2\2K\u01d8\3\2\2\2")
        buf.write("M\u01da\3\2\2\2O\u01e1\3\2\2\2Q\u01e8\3\2\2\2S\u01f1\3")
        buf.write("\2\2\2U\u01f5\3\2\2\2W\u01f9\3\2\2\2Y\u01fb\3\2\2\2[\u01ff")
        buf.write("\3\2\2\2]\u0201\3\2\2\2_\u0204\3\2\2\2a\u0207\3\2\2\2")
        buf.write("c\u0209\3\2\2\2e\u020b\3\2\2\2g\u020d\3\2\2\2i\u0210\3")
        buf.write("\2\2\2k\u0212\3\2\2\2m\u0215\3\2\2\2o\u0218\3\2\2\2q\u021a")
        buf.write("\3\2\2\2s\u021c\3\2\2\2u\u021e\3\2\2\2w\u0221\3\2\2\2")
        buf.write("y\u0224\3\2\2\2{\u0226\3\2\2\2}\u0228\3\2\2\2\177\u022a")
        buf.write("\3\2\2\2\u0081\u022c\3\2\2\2\u0083\u022f\3\2\2\2\u0085")
        buf.write("\u0231\3\2\2\2\u0087\u0234\3\2\2\2\u0089\u0237\3\2\2\2")
        buf.write("\u008b\u0239\3\2\2\2\u008d\u023b\3\2\2\2\u008f\u023e\3")
        buf.write("\2\2\2\u0091\u0241\3\2\2\2\u0093\u0244\3\2\2\2\u0095\u0247")
        buf.write("\3\2\2\2\u0097\u024a\3\2\2\2\u0099\u024c\3\2\2\2\u009b")
        buf.write("\u024f\3\2\2\2\u009d\u0252\3\2\2\2\u009f\u0255\3\2\2\2")
        buf.write("\u00a1\u0258\3\2\2\2\u00a3\u025b\3\2\2\2\u00a5\u025e\3")
        buf.write("\2\2\2\u00a7\u0261\3\2\2\2\u00a9\u0264\3\2\2\2\u00ab\u0267")
        buf.write("\3\2\2\2\u00ad\u026a\3\2\2\2\u00af\u026e\3\2\2\2\u00b1")
        buf.write("\u0272\3\2\2\2\u00b3\u0276\3\2\2\2\u00b5\u027d\3\2\2\2")
        buf.write("\u00b7\u0281\3\2\2\2\u00b9\u0295\3\2\2\2\u00bb\u02b1\3")
        buf.write("\2\2\2\u00bd\u02b5\3\2\2\2\u00bf\u02b7\3\2\2\2\u00c1\u02b9")
        buf.write("\3\2\2\2\u00c3\u02bc\3\2\2\2\u00c5\u02be\3\2\2\2\u00c7")
        buf.write("\u02c0\3\2\2\2\u00c9\u02c2\3\2\2\2\u00cb\u02c4\3\2\2\2")
        buf.write("\u00cd\u02cd\3\2\2\2\u00cf\u02d1\3\2\2\2\u00d1\u02d6\3")
        buf.write("\2\2\2\u00d3\u02da\3\2\2\2\u00d5\u02e0\3\2\2\2\u00d7\u02fb")
        buf.write("\3\2\2\2\u00d9\u0317\3\2\2\2\u00db\u031b\3\2\2\2\u00dd")
        buf.write("\u031e\3\2\2\2\u00df\u0321\3\2\2\2\u00e1\u0324\3\2\2\2")
        buf.write("\u00e3\u0326\3\2\2\2\u00e5\u032a\3\2\2\2\u00e7\u032e\3")
        buf.write("\2\2\2\u00e9\u0335\3\2\2\2\u00eb\u0341\3\2\2\2\u00ed\u0345")
        buf.write("\3\2\2\2\u00ef\u00f0\7f\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7h\2\2\u00f2\4\3\2\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8\u00f9\7p\2\2\u00f9\6\3\2\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe")
        buf.write("\7u\2\2\u00fe\u00ff\7g\2\2\u00ff\b\3\2\2\2\u0100\u0101")
        buf.write("\7h\2\2\u0101\u0102\7t\2\2\u0102\u0103\7q\2\2\u0103\u0104")
        buf.write("\7o\2\2\u0104\n\3\2\2\2\u0105\u0106\7k\2\2\u0106\u0107")
        buf.write("\7o\2\2\u0107\u0108\7r\2\2\u0108\u0109\7q\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\u010b\7v\2\2\u010b\f\3\2\2\2\u010c\u010d")
        buf.write("\7c\2\2\u010d\u010e\7u\2\2\u010e\16\3\2\2\2\u010f\u0110")
        buf.write("\7i\2\2\u0110\u0111\7n\2\2\u0111\u0112\7q\2\2\u0112\u0113")
        buf.write("\7d\2\2\u0113\u0114\7c\2\2\u0114\u0115\7n\2\2\u0115\20")
        buf.write("\3\2\2\2\u0116\u0117\7p\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7n\2\2\u011a\u011b\7q\2\2\u011b\u011c")
        buf.write("\7e\2\2\u011c\u011d\7c\2\2\u011d\u011e\7n\2\2\u011e\22")
        buf.write("\3\2\2\2\u011f\u0120\7c\2\2\u0120\u0121\7u\2\2\u0121\u0122")
        buf.write("\7u\2\2\u0122\u0123\7g\2\2\u0123\u0124\7t\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\24\3\2\2\2\u0126\u0127\7k\2\2\u0127\u0128")
        buf.write("\7h\2\2\u0128\26\3\2\2\2\u0129\u012a\7g\2\2\u012a\u012b")
        buf.write("\7n\2\2\u012b\u012c\7k\2\2\u012c\u012d\7h\2\2\u012d\30")
        buf.write("\3\2\2\2\u012e\u012f\7g\2\2\u012f\u0130\7n\2\2\u0130\u0131")
        buf.write("\7u\2\2\u0131\u0132\7g\2\2\u0132\32\3\2\2\2\u0133\u0134")
        buf.write("\7y\2\2\u0134\u0135\7j\2\2\u0135\u0136\7k\2\2\u0136\u0137")
        buf.write("\7n\2\2\u0137\u0138\7g\2\2\u0138\34\3\2\2\2\u0139\u013a")
        buf.write("\7h\2\2\u013a\u013b\7q\2\2\u013b\u013c\7t\2\2\u013c\36")
        buf.write("\3\2\2\2\u013d\u013e\7k\2\2\u013e\u013f\7p\2\2\u013f ")
        buf.write("\3\2\2\2\u0140\u0141\7v\2\2\u0141\u0142\7t\2\2\u0142\u0143")
        buf.write("\7{\2\2\u0143\"\3\2\2\2\u0144\u0145\7h\2\2\u0145\u0146")
        buf.write("\7k\2\2\u0146\u0147\7p\2\2\u0147\u0148\7c\2\2\u0148\u0149")
        buf.write("\7n\2\2\u0149\u014a\7n\2\2\u014a\u014b\7{\2\2\u014b$\3")
        buf.write("\2\2\2\u014c\u014d\7y\2\2\u014d\u014e\7k\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f\u0150\7j\2\2\u0150&\3\2\2\2\u0151\u0152")
        buf.write("\7g\2\2\u0152\u0153\7z\2\2\u0153\u0154\7e\2\2\u0154\u0155")
        buf.write("\7g\2\2\u0155\u0156\7r\2\2\u0156\u0157\7v\2\2\u0157(\3")
        buf.write("\2\2\2\u0158\u0159\7n\2\2\u0159\u015a\7c\2\2\u015a\u015b")
        buf.write("\7o\2\2\u015b\u015c\7d\2\2\u015c\u015d\7f\2\2\u015d\u015e")
        buf.write("\7c\2\2\u015e*\3\2\2\2\u015f\u0160\7q\2\2\u0160\u0161")
        buf.write("\7t\2\2\u0161,\3\2\2\2\u0162\u0163\7c\2\2\u0163\u0164")
        buf.write("\7p\2\2\u0164\u0165\7f\2\2\u0165.\3\2\2\2\u0166\u0167")
        buf.write("\7p\2\2\u0167\u0168\7q\2\2\u0168\u0169\7v\2\2\u0169\60")
        buf.write("\3\2\2\2\u016a\u016b\7k\2\2\u016b\u016c\7u\2\2\u016c\62")
        buf.write("\3\2\2\2\u016d\u016e\7P\2\2\u016e\u016f\7q\2\2\u016f\u0170")
        buf.write("\7p\2\2\u0170\u0171\7g\2\2\u0171\64\3\2\2\2\u0172\u0173")
        buf.write("\7V\2\2\u0173\u0174\7t\2\2\u0174\u0175\7w\2\2\u0175\u0176")
        buf.write("\7g\2\2\u0176\66\3\2\2\2\u0177\u0178\7H\2\2\u0178\u0179")
        buf.write("\7c\2\2\u0179\u017a\7n\2\2\u017a\u017b\7u\2\2\u017b\u017c")
        buf.write("\7g\2\2\u017c8\3\2\2\2\u017d\u017e\7e\2\2\u017e\u017f")
        buf.write("\7n\2\2\u017f\u0180\7c\2\2\u0180\u0181\7u\2\2\u0181\u0182")
        buf.write("\7u\2\2\u0182:\3\2\2\2\u0183\u0184\7{\2\2\u0184\u0185")
        buf.write("\7k\2\2\u0185\u0186\7g\2\2\u0186\u0187\7n\2\2\u0187\u0188")
        buf.write("\7f\2\2\u0188<\3\2\2\2\u0189\u018a\7f\2\2\u018a\u018b")
        buf.write("\7g\2\2\u018b\u018c\7n\2\2\u018c>\3\2\2\2\u018d\u018e")
        buf.write("\7r\2\2\u018e\u018f\7c\2\2\u018f\u0190\7u\2\2\u0190\u0191")
        buf.write("\7u\2\2\u0191@\3\2\2\2\u0192\u0193\7e\2\2\u0193\u0194")
        buf.write("\7q\2\2\u0194\u0195\7p\2\2\u0195\u0196\7v\2\2\u0196\u0197")
        buf.write("\7k\2\2\u0197\u0198\7p\2\2\u0198\u0199\7w\2\2\u0199\u019a")
        buf.write("\7g\2\2\u019aB\3\2\2\2\u019b\u019c\7d\2\2\u019c\u019d")
        buf.write("\7t\2\2\u019d\u019e\7g\2\2\u019e\u019f\7c\2\2\u019f\u01a0")
        buf.write("\7m\2\2\u01a0D\3\2\2\2\u01a1\u01a2\6#\2\2\u01a2\u01ae")
        buf.write("\5\u00e5s\2\u01a3\u01a5\7\17\2\2\u01a4\u01a3\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a9\7\f\2\2")
        buf.write("\u01a7\u01a9\7\17\2\2\u01a8\u01a4\3\2\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01ac\5\u00e5s\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2")
        buf.write("\u01ad\u01a1\3\2\2\2\u01ad\u01a8\3\2\2\2\u01ae\u01af\3")
        buf.write("\2\2\2\u01af\u01b0\b#\2\2\u01b0F\3\2\2\2\u01b1\u01b5\5")
        buf.write("\u00ebv\2\u01b2\u01b4\5\u00edw\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6H\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01ba\t\2\2")
        buf.write("\2\u01b9\u01b8\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc")
        buf.write("\3\2\2\2\u01bb\u01bd\t\3\2\2\u01bc\u01bb\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01c1\5\u00b9")
        buf.write("]\2\u01bf\u01c1\5\u00bb^\2\u01c0\u01be\3\2\2\2\u01c0\u01bf")
        buf.write("\3\2\2\2\u01c1\u01cb\3\2\2\2\u01c2\u01c4\t\4\2\2\u01c3")
        buf.write("\u01c5\t\3\2\2\u01c4\u01c3\3\2\2\2\u01c4\u01c5\3\2\2\2")
        buf.write("\u01c5\u01c8\3\2\2\2\u01c6\u01c9\5\u00d7l\2\u01c7\u01c9")
        buf.write("\5\u00d9m\2\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9")
        buf.write("\u01cb\3\2\2\2\u01ca\u01b9\3\2\2\2\u01ca\u01c2\3\2\2\2")
        buf.write("\u01cbJ\3\2\2\2\u01cc\u01d0\5\u00c3b\2\u01cd\u01cf\5\u00c5")
        buf.write("c\2\u01ce\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce")
        buf.write("\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d9\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d3\u01d5\7\62\2\2\u01d4\u01d3\3\2\2")
        buf.write("\2\u01d5\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01cc\3\2\2\2\u01d8")
        buf.write("\u01d4\3\2\2\2\u01d9L\3\2\2\2\u01da\u01db\7\62\2\2\u01db")
        buf.write("\u01dd\t\5\2\2\u01dc\u01de\5\u00c7d\2\u01dd\u01dc\3\2")
        buf.write("\2\2\u01de\u01df\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0N\3\2\2\2\u01e1\u01e2\7\62\2\2\u01e2\u01e4")
        buf.write("\t\6\2\2\u01e3\u01e5\5\u00c9e\2\u01e4\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2")
        buf.write("\u01e7P\3\2\2\2\u01e8\u01e9\7\62\2\2\u01e9\u01eb\t\4\2")
        buf.write("\2\u01ea\u01ec\5\u00cbf\2\u01eb\u01ea\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write("R\3\2\2\2\u01ef\u01f2\5\u00cdg\2\u01f0\u01f2\5\u00cfh")
        buf.write("\2\u01f1\u01ef\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2T\3\2")
        buf.write("\2\2\u01f3\u01f6\5S*\2\u01f4\u01f6\5\u00d1i\2\u01f5\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f8\t\7\2\2\u01f8V\3\2\2\2\u01f9\u01fa\7\60\2\2\u01fa")
        buf.write("X\3\2\2\2\u01fb\u01fc\7\60\2\2\u01fc\u01fd\7\60\2\2\u01fd")
        buf.write("\u01fe\7\60\2\2\u01feZ\3\2\2\2\u01ff\u0200\7,\2\2\u0200")
        buf.write("\\\3\2\2\2\u0201\u0202\7*\2\2\u0202\u0203\b/\3\2\u0203")
        buf.write("^\3\2\2\2\u0204\u0205\7+\2\2\u0205\u0206\b\60\4\2\u0206")
        buf.write("`\3\2\2\2\u0207\u0208\7.\2\2\u0208b\3\2\2\2\u0209\u020a")
        buf.write("\7<\2\2\u020ad\3\2\2\2\u020b\u020c\7=\2\2\u020cf\3\2\2")
        buf.write("\2\u020d\u020e\7,\2\2\u020e\u020f\7,\2\2\u020fh\3\2\2")
        buf.write("\2\u0210\u0211\7?\2\2\u0211j\3\2\2\2\u0212\u0213\7]\2")
        buf.write("\2\u0213\u0214\b\66\5\2\u0214l\3\2\2\2\u0215\u0216\7_")
        buf.write("\2\2\u0216\u0217\b\67\6\2\u0217n\3\2\2\2\u0218\u0219\7")
        buf.write("~\2\2\u0219p\3\2\2\2\u021a\u021b\7`\2\2\u021br\3\2\2\2")
        buf.write("\u021c\u021d\7(\2\2\u021dt\3\2\2\2\u021e\u021f\7>\2\2")
        buf.write("\u021f\u0220\7>\2\2\u0220v\3\2\2\2\u0221\u0222\7@\2\2")
        buf.write("\u0222\u0223\7@\2\2\u0223x\3\2\2\2\u0224\u0225\7-\2\2")
        buf.write("\u0225z\3\2\2\2\u0226\u0227\7/\2\2\u0227|\3\2\2\2\u0228")
        buf.write("\u0229\7\61\2\2\u0229~\3\2\2\2\u022a\u022b\7\'\2\2\u022b")
        buf.write("\u0080\3\2\2\2\u022c\u022d\7\61\2\2\u022d\u022e\7\61\2")
        buf.write("\2\u022e\u0082\3\2\2\2\u022f\u0230\7\u0080\2\2\u0230\u0084")
        buf.write("\3\2\2\2\u0231\u0232\7}\2\2\u0232\u0233\bC\7\2\u0233\u0086")
        buf.write("\3\2\2\2\u0234\u0235\7\177\2\2\u0235\u0236\bD\b\2\u0236")
        buf.write("\u0088\3\2\2\2\u0237\u0238\7>\2\2\u0238\u008a\3\2\2\2")
        buf.write("\u0239\u023a\7@\2\2\u023a\u008c\3\2\2\2\u023b\u023c\7")
        buf.write("?\2\2\u023c\u023d\7?\2\2\u023d\u008e\3\2\2\2\u023e\u023f")
        buf.write("\7@\2\2\u023f\u0240\7?\2\2\u0240\u0090\3\2\2\2\u0241\u0242")
        buf.write("\7>\2\2\u0242\u0243\7?\2\2\u0243\u0092\3\2\2\2\u0244\u0245")
        buf.write("\7>\2\2\u0245\u0246\7@\2\2\u0246\u0094\3\2\2\2\u0247\u0248")
        buf.write("\7#\2\2\u0248\u0249\7?\2\2\u0249\u0096\3\2\2\2\u024a\u024b")
        buf.write("\7B\2\2\u024b\u0098\3\2\2\2\u024c\u024d\7/\2\2\u024d\u024e")
        buf.write("\7@\2\2\u024e\u009a\3\2\2\2\u024f\u0250\7-\2\2\u0250\u0251")
        buf.write("\7?\2\2\u0251\u009c\3\2\2\2\u0252\u0253\7/\2\2\u0253\u0254")
        buf.write("\7?\2\2\u0254\u009e\3\2\2\2\u0255\u0256\7,\2\2\u0256\u0257")
        buf.write("\7?\2\2\u0257\u00a0\3\2\2\2\u0258\u0259\7B\2\2\u0259\u025a")
        buf.write("\7?\2\2\u025a\u00a2\3\2\2\2\u025b\u025c\7\61\2\2\u025c")
        buf.write("\u025d\7?\2\2\u025d\u00a4\3\2\2\2\u025e\u025f\7\'\2\2")
        buf.write("\u025f\u0260\7?\2\2\u0260\u00a6\3\2\2\2\u0261\u0262\7")
        buf.write("(\2\2\u0262\u0263\7?\2\2\u0263\u00a8\3\2\2\2\u0264\u0265")
        buf.write("\7~\2\2\u0265\u0266\7?\2\2\u0266\u00aa\3\2\2\2\u0267\u0268")
        buf.write("\7`\2\2\u0268\u0269\7?\2\2\u0269\u00ac\3\2\2\2\u026a\u026b")
        buf.write("\7>\2\2\u026b\u026c\7>\2\2\u026c\u026d\7?\2\2\u026d\u00ae")
        buf.write("\3\2\2\2\u026e\u026f\7@\2\2\u026f\u0270\7@\2\2\u0270\u0271")
        buf.write("\7?\2\2\u0271\u00b0\3\2\2\2\u0272\u0273\7,\2\2\u0273\u0274")
        buf.write("\7,\2\2\u0274\u0275\7?\2\2\u0275\u00b2\3\2\2\2\u0276\u0277")
        buf.write("\7\61\2\2\u0277\u0278\7\61\2\2\u0278\u0279\7?\2\2\u0279")
        buf.write("\u00b4\3\2\2\2\u027a\u027e\5\u00e5s\2\u027b\u027e\5\u00e7")
        buf.write("t\2\u027c\u027e\5\u00e9u\2\u027d\u027a\3\2\2\2\u027d\u027b")
        buf.write("\3\2\2\2\u027d\u027c\3\2\2\2\u027e\u027f\3\2\2\2\u027f")
        buf.write("\u0280\b[\t\2\u0280\u00b6\3\2\2\2\u0281\u0282\13\2\2\2")
        buf.write("\u0282\u00b8\3\2\2\2\u0283\u0288\7)\2\2\u0284\u0287\5")
        buf.write("\u00c1a\2\u0285\u0287\n\b\2\2\u0286\u0284\3\2\2\2\u0286")
        buf.write("\u0285\3\2\2\2\u0287\u028a\3\2\2\2\u0288\u0286\3\2\2\2")
        buf.write("\u0288\u0289\3\2\2\2\u0289\u028b\3\2\2\2\u028a\u0288\3")
        buf.write("\2\2\2\u028b\u0296\7)\2\2\u028c\u0291\7$\2\2\u028d\u0290")
        buf.write("\5\u00c1a\2\u028e\u0290\n\t\2\2\u028f\u028d\3\2\2\2\u028f")
        buf.write("\u028e\3\2\2\2\u0290\u0293\3\2\2\2\u0291\u028f\3\2\2\2")
        buf.write("\u0291\u0292\3\2\2\2\u0292\u0294\3\2\2\2\u0293\u0291\3")
        buf.write("\2\2\2\u0294\u0296\7$\2\2\u0295\u0283\3\2\2\2\u0295\u028c")
        buf.write("\3\2\2\2\u0296\u00ba\3\2\2\2\u0297\u0298\7)\2\2\u0298")
        buf.write("\u0299\7)\2\2\u0299\u029a\7)\2\2\u029a\u029e\3\2\2\2\u029b")
        buf.write("\u029d\5\u00bd_\2\u029c\u029b\3\2\2\2\u029d\u02a0\3\2")
        buf.write("\2\2\u029e\u029f\3\2\2\2\u029e\u029c\3\2\2\2\u029f\u02a1")
        buf.write("\3\2\2\2\u02a0\u029e\3\2\2\2\u02a1\u02a2\7)\2\2\u02a2")
        buf.write("\u02a3\7)\2\2\u02a3\u02b2\7)\2\2\u02a4\u02a5\7$\2\2\u02a5")
        buf.write("\u02a6\7$\2\2\u02a6\u02a7\7$\2\2\u02a7\u02ab\3\2\2\2\u02a8")
        buf.write("\u02aa\5\u00bd_\2\u02a9\u02a8\3\2\2\2\u02aa\u02ad\3\2")
        buf.write("\2\2\u02ab\u02ac\3\2\2\2\u02ab\u02a9\3\2\2\2\u02ac\u02ae")
        buf.write("\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ae\u02af\7$\2\2\u02af")
        buf.write("\u02b0\7$\2\2\u02b0\u02b2\7$\2\2\u02b1\u0297\3\2\2\2\u02b1")
        buf.write("\u02a4\3\2\2\2\u02b2\u00bc\3\2\2\2\u02b3\u02b6\5\u00bf")
        buf.write("`\2\u02b4\u02b6\5\u00c1a\2\u02b5\u02b3\3\2\2\2\u02b5\u02b4")
        buf.write("\3\2\2\2\u02b6\u00be\3\2\2\2\u02b7\u02b8\n\n\2\2\u02b8")
        buf.write("\u00c0\3\2\2\2\u02b9\u02ba\7^\2\2\u02ba\u02bb\13\2\2\2")
        buf.write("\u02bb\u00c2\3\2\2\2\u02bc\u02bd\t\13\2\2\u02bd\u00c4")
        buf.write("\3\2\2\2\u02be\u02bf\t\f\2\2\u02bf\u00c6\3\2\2\2\u02c0")
        buf.write("\u02c1\t\r\2\2\u02c1\u00c8\3\2\2\2\u02c2\u02c3\t\16\2")
        buf.write("\2\u02c3\u00ca\3\2\2\2\u02c4\u02c5\t\17\2\2\u02c5\u00cc")
        buf.write("\3\2\2\2\u02c6\u02c8\5\u00d1i\2\u02c7\u02c6\3\2\2\2\u02c7")
        buf.write("\u02c8\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02ce\5\u00d3")
        buf.write("j\2\u02ca\u02cb\5\u00d1i\2\u02cb\u02cc\7\60\2\2\u02cc")
        buf.write("\u02ce\3\2\2\2\u02cd\u02c7\3\2\2\2\u02cd\u02ca\3\2\2\2")
        buf.write("\u02ce\u00ce\3\2\2\2\u02cf\u02d2\5\u00d1i\2\u02d0\u02d2")
        buf.write("\5\u00cdg\2\u02d1\u02cf\3\2\2\2\u02d1\u02d0\3\2\2\2\u02d2")
        buf.write("\u02d3\3\2\2\2\u02d3\u02d4\5\u00d5k\2\u02d4\u00d0\3\2")
        buf.write("\2\2\u02d5\u02d7\5\u00c5c\2\u02d6\u02d5\3\2\2\2\u02d7")
        buf.write("\u02d8\3\2\2\2\u02d8\u02d6\3\2\2\2\u02d8\u02d9\3\2\2\2")
        buf.write("\u02d9\u00d2\3\2\2\2\u02da\u02dc\7\60\2\2\u02db\u02dd")
        buf.write("\5\u00c5c\2\u02dc\u02db\3\2\2\2\u02dd\u02de\3\2\2\2\u02de")
        buf.write("\u02dc\3\2\2\2\u02de\u02df\3\2\2\2\u02df\u00d4\3\2\2\2")
        buf.write("\u02e0\u02e2\t\20\2\2\u02e1\u02e3\t\21\2\2\u02e2\u02e1")
        buf.write("\3\2\2\2\u02e2\u02e3\3\2\2\2\u02e3\u02e5\3\2\2\2\u02e4")
        buf.write("\u02e6\5\u00c5c\2\u02e5\u02e4\3\2\2\2\u02e6\u02e7\3\2")
        buf.write("\2\2\u02e7\u02e5\3\2\2\2\u02e7\u02e8\3\2\2\2\u02e8\u00d6")
        buf.write("\3\2\2\2\u02e9\u02ee\7)\2\2\u02ea\u02ed\5\u00ddo\2\u02eb")
        buf.write("\u02ed\5\u00e3r\2\u02ec\u02ea\3\2\2\2\u02ec\u02eb\3\2")
        buf.write("\2\2\u02ed\u02f0\3\2\2\2\u02ee\u02ec\3\2\2\2\u02ee\u02ef")
        buf.write("\3\2\2\2\u02ef\u02f1\3\2\2\2\u02f0\u02ee\3\2\2\2\u02f1")
        buf.write("\u02fc\7)\2\2\u02f2\u02f7\7$\2\2\u02f3\u02f6\5\u00dfp")
        buf.write("\2\u02f4\u02f6\5\u00e3r\2\u02f5\u02f3\3\2\2\2\u02f5\u02f4")
        buf.write("\3\2\2\2\u02f6\u02f9\3\2\2\2\u02f7\u02f5\3\2\2\2\u02f7")
        buf.write("\u02f8\3\2\2\2\u02f8\u02fa\3\2\2\2\u02f9\u02f7\3\2\2\2")
        buf.write("\u02fa\u02fc\7$\2\2\u02fb\u02e9\3\2\2\2\u02fb\u02f2\3")
        buf.write("\2\2\2\u02fc\u00d8\3\2\2\2\u02fd\u02fe\7)\2\2\u02fe\u02ff")
        buf.write("\7)\2\2\u02ff\u0300\7)\2\2\u0300\u0304\3\2\2\2\u0301\u0303")
        buf.write("\5\u00dbn\2\u0302\u0301\3\2\2\2\u0303\u0306\3\2\2\2\u0304")
        buf.write("\u0305\3\2\2\2\u0304\u0302\3\2\2\2\u0305\u0307\3\2\2\2")
        buf.write("\u0306\u0304\3\2\2\2\u0307\u0308\7)\2\2\u0308\u0309\7")
        buf.write(")\2\2\u0309\u0318\7)\2\2\u030a\u030b\7$\2\2\u030b\u030c")
        buf.write("\7$\2\2\u030c\u030d\7$\2\2\u030d\u0311\3\2\2\2\u030e\u0310")
        buf.write("\5\u00dbn\2\u030f\u030e\3\2\2\2\u0310\u0313\3\2\2\2\u0311")
        buf.write("\u0312\3\2\2\2\u0311\u030f\3\2\2\2\u0312\u0314\3\2\2\2")
        buf.write("\u0313\u0311\3\2\2\2\u0314\u0315\7$\2\2\u0315\u0316\7")
        buf.write("$\2\2\u0316\u0318\7$\2\2\u0317\u02fd\3\2\2\2\u0317\u030a")
        buf.write("\3\2\2\2\u0318\u00da\3\2\2\2\u0319\u031c\5\u00e1q\2\u031a")
        buf.write("\u031c\5\u00e3r\2\u031b\u0319\3\2\2\2\u031b\u031a\3\2")
        buf.write("\2\2\u031c\u00dc\3\2\2\2\u031d\u031f\t\22\2\2\u031e\u031d")
        buf.write("\3\2\2\2\u031f\u00de\3\2\2\2\u0320\u0322\t\23\2\2\u0321")
        buf.write("\u0320\3\2\2\2\u0322\u00e0\3\2\2\2\u0323\u0325\t\24\2")
        buf.write("\2\u0324\u0323\3\2\2\2\u0325\u00e2\3\2\2\2\u0326\u0327")
        buf.write("\7^\2\2\u0327\u0328\t\25\2\2\u0328\u00e4\3\2\2\2\u0329")
        buf.write("\u032b\t\26\2\2\u032a\u0329\3\2\2\2\u032b\u032c\3\2\2")
        buf.write("\2\u032c\u032a\3\2\2\2\u032c\u032d\3\2\2\2\u032d\u00e6")
        buf.write("\3\2\2\2\u032e\u0332\7%\2\2\u032f\u0331\n\27\2\2\u0330")
        buf.write("\u032f\3\2\2\2\u0331\u0334\3\2\2\2\u0332\u0330\3\2\2\2")
        buf.write("\u0332\u0333\3\2\2\2\u0333\u00e8\3\2\2\2\u0334\u0332\3")
        buf.write("\2\2\2\u0335\u0337\7^\2\2\u0336\u0338\5\u00e5s\2\u0337")
        buf.write("\u0336\3\2\2\2\u0337\u0338\3\2\2\2\u0338\u033e\3\2\2\2")
        buf.write("\u0339\u033b\7\17\2\2\u033a\u0339\3\2\2\2\u033a\u033b")
        buf.write("\3\2\2\2\u033b\u033c\3\2\2\2\u033c\u033f\7\f\2\2\u033d")
        buf.write("\u033f\7\17\2\2\u033e\u033a\3\2\2\2\u033e\u033d\3\2\2")
        buf.write("\2\u033f\u00ea\3\2\2\2\u0340\u0342\t\30\2\2\u0341\u0340")
        buf.write("\3\2\2\2\u0342\u00ec\3\2\2\2\u0343\u0346\5\u00ebv\2\u0344")
        buf.write("\u0346\t\31\2\2\u0345\u0343\3\2\2\2\u0345\u0344\3\2\2")
        buf.write("\2\u0346\u00ee\3\2\2\2:\2\u01a4\u01a8\u01ab\u01ad\u01b5")
        buf.write("\u01b9\u01bc\u01c0\u01c4\u01c8\u01ca\u01d0\u01d6\u01d8")
        buf.write("\u01df\u01e6\u01ed\u01f1\u01f5\u027d\u0286\u0288\u028f")
        buf.write("\u0291\u0295\u029e\u02ab\u02b1\u02b5\u02c7\u02cd\u02d1")
        buf.write("\u02d8\u02de\u02e2\u02e7\u02ec\u02ee\u02f5\u02f7\u02fb")
        buf.write("\u0304\u0311\u0317\u031b\u031e\u0321\u0324\u032c\u0332")
        buf.write("\u0337\u033a\u033e\u0341\u0345\n\3#\2\3/\3\3\60\4\3\66")
        buf.write("\5\3\67\6\3C\7\3D\b\b\2\2")
        return buf.getvalue()


class Python3Lexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    DEF = 1
    RETURN = 2
    RAISE = 3
    FROM = 4
    IMPORT = 5
    AS = 6
    GLOBAL = 7
    NONLOCAL = 8
    ASSERT = 9
    IF = 10
    ELIF = 11
    ELSE = 12
    WHILE = 13
    FOR = 14
    IN = 15
    TRY = 16
    FINALLY = 17
    WITH = 18
    EXCEPT = 19
    LAMBDA = 20
    OR = 21
    AND = 22
    NOT = 23
    IS = 24
    NONE = 25
    TRUE = 26
    FALSE = 27
    CLASS = 28
    YIELD = 29
    DEL = 30
    PASS = 31
    CONTINUE = 32
    BREAK = 33
    NEWLINE = 34
    NAME = 35
    STRING_BYTES_LITERAL = 36
    DECIMAL_INTEGER = 37
    OCT_INTEGER = 38
    HEX_INTEGER = 39
    BIN_INTEGER = 40
    FLOAT_NUMBER = 41
    IMAG_NUMBER = 42
    DOT = 43
    ELLIPSIS = 44
    STAR = 45
    OPEN_PAREN = 46
    CLOSE_PAREN = 47
    COMMA = 48
    COLON = 49
    SEMI_COLON = 50
    POWER = 51
    ASSIGN = 52
    OPEN_BRACK = 53
    CLOSE_BRACK = 54
    OR_OP = 55
    XOR = 56
    AND_OP = 57
    LEFT_SHIFT = 58
    RIGHT_SHIFT = 59
    ADD = 60
    MINUS = 61
    DIV = 62
    MOD = 63
    IDIV = 64
    NOT_OP = 65
    OPEN_BRACE = 66
    CLOSE_BRACE = 67
    LESS_THAN = 68
    GREATER_THAN = 69
    EQUALS = 70
    GT_EQ = 71
    LT_EQ = 72
    NOT_EQ_1 = 73
    NOT_EQ_2 = 74
    AT = 75
    ARROW = 76
    ADD_ASSIGN = 77
    SUB_ASSIGN = 78
    MULT_ASSIGN = 79
    AT_ASSIGN = 80
    DIV_ASSIGN = 81
    MOD_ASSIGN = 82
    AND_ASSIGN = 83
    OR_ASSIGN = 84
    XOR_ASSIGN = 85
    LEFT_SHIFT_ASSIGN = 86
    RIGHT_SHIFT_ASSIGN = 87
    POWER_ASSIGN = 88
    IDIV_ASSIGN = 89
    SKIP_ = 90
    UNKNOWN_CHAR = 91

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'def'", "'return'", "'raise'", "'from'", "'import'", "'as'",
                    "'global'", "'nonlocal'", "'assert'", "'if'", "'elif'", "'else'",
                    "'while'", "'for'", "'in'", "'try'", "'finally'", "'with'",
                    "'except'", "'lambda'", "'or'", "'and'", "'not'", "'is'", "'None'",
                    "'True'", "'False'", "'class'", "'yield'", "'del'", "'pass'",
                    "'continue'", "'break'", "'.'", "'...'", "'*'", "'('", "')'",
                    "','", "':'", "';'", "'**'", "'='", "'['", "']'", "'|'", "'^'",
                    "'&'", "'<<'", "'>>'", "'+'", "'-'", "'/'", "'%'", "'//'", "'~'",
                    "'{'", "'}'", "'<'", "'>'", "'=='", "'>='", "'<='", "'<>'",
                    "'!='", "'@'", "'->'", "'+='", "'-='", "'*='", "'@='", "'/='",
                    "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", "'//='"]

    symbolicNames = ["<INVALID>",
                     "DEF", "RETURN", "RAISE", "FROM", "IMPORT", "AS", "GLOBAL",
                     "NONLOCAL", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", "FOR",
                     "IN", "TRY", "FINALLY", "WITH", "EXCEPT", "LAMBDA", "OR", "AND",
                     "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "YIELD", "DEL",
                     "PASS", "CONTINUE", "BREAK", "NEWLINE", "NAME", "STRING_BYTES_LITERAL",
                     "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER",
                     "FLOAT_NUMBER", "IMAG_NUMBER", "DOT", "ELLIPSIS", "STAR", "OPEN_PAREN",
                     "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN",
                     "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT",
                     "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "MOD", "IDIV", "NOT_OP",
                     "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS",
                     "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN",
                     "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN",
                     "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN",
                     "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_",
                     "UNKNOWN_CHAR"]

    ruleNames = ["DEF", "RETURN", "RAISE", "FROM", "IMPORT", "AS", "GLOBAL",
                 "NONLOCAL", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", "FOR",
                 "IN", "TRY", "FINALLY", "WITH", "EXCEPT", "LAMBDA", "OR",
                 "AND", "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS",
                 "YIELD", "DEL", "PASS", "CONTINUE", "BREAK", "NEWLINE",
                 "NAME", "STRING_BYTES_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER",
                 "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER",
                 "DOT", "ELLIPSIS", "STAR", "OPEN_PAREN", "CLOSE_PAREN",
                 "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", "OPEN_BRACK",
                 "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT",
                 "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "MOD", "IDIV", "NOT_OP",
                 "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN",
                 "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT",
                 "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN",
                 "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN",
                 "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN",
                 "POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", "UNKNOWN_CHAR",
                 "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", "LONG_STRING_CHAR",
                 "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT",
                 "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", "EXPONENT_FLOAT",
                 "INT_PART", "FRACTION", "EXPONENT", "SHORT_BYTES", "LONG_BYTES",
                 "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE",
                 "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", "LONG_BYTES_CHAR",
                 "BYTES_ESCAPE_SEQ", "SPACES", "COMMENT", "LINE_JOINING",
                 "ID_START", "ID_CONTINUE"]

    grammarFileName = "Python3.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

    @property
    def tokens(self):
        if not hasattr(self, "_tokens"):
            self._tokens = []
        return self._tokens

    @property
    def indents(self):
        if not hasattr(self, "_indents"):
            self._indents = []
        return self._indents

    @property
    def opened(self):
        if not hasattr(self, "_opened"):
            self._opened = 0
        return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value

    @property
    def lastToken(self):
        if not hasattr(self, "_lastToken"):
            self._lastToken = None
        return self._lastToken

    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value

    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None

    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)

    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens) - 1, -1, -1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)

            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()

            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)

    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent

    def commonToken(self, type, text):
        stop = self.getCharIndex() - 1
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count

    def atStartOfInput(self):
        return self.column == 0 and self.line == 1

    def action(self, localctx: RuleContext, ruleIndex: int, actionIndex: int):
        if self._actions is None:
            actions = dict()
            actions[33] = self.NEWLINE_action
            actions[45] = self.OPEN_PAREN_action
            actions[46] = self.CLOSE_PAREN_action
            actions[52] = self.OPEN_BRACK_action
            actions[53] = self.CLOSE_BRACK_action
            actions[65] = self.OPEN_BRACE_action
            actions[66] = self.CLOSE_BRACE_action
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 0:

            tempt = self.text
            newLine = re.sub("[^\r\n]+", "", tempt)
            spaces = re.sub("[\r\n]+", "", tempt)
            next = chr(self._input.LA(1))

            if self.opened > 0 or next in ['\r', '\n', '#']:
                self.skip()
            else:
                self.emitToken(self.commonToken(self.NEWLINE, newLine))
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0

                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()

    def OPEN_PAREN_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 1:
            self.opened += 1

    def CLOSE_PAREN_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 2:
            self.opened -= 1

    def OPEN_BRACK_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 3:
            self.opened += 1

    def CLOSE_BRACK_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 4:
            self.opened -= 1

    def OPEN_BRACE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 5:
            self.opened += 1

    def CLOSE_BRACE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 6:
            self.opened -= 1

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates is None:
            preds = dict()
            preds[33] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx: RuleContext, predIndex: int):
        if predIndex == 0:
            return self.atStartOfInput()
