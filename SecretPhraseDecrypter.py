# Author: Vikas Yadav

############ AI HELP WORK STRARTED HERE ############
# This keyboardSymbols is created using AI and is based on the standard US QWERTY keyboard layout. 
# It maps each symbol that can be typed using the Shift key to its corresponding unshifted symbol. 
# For example, "!" is mapped to "1", "@" is mapped to "2", and so on. 
# This mapping allows us to decode a secret phrase by replacing the symbols with their corresponding characters.
keyboardSymbols = {
    "!": "1", #(Exclamation/One)
    "@": "2", #(At/Two)
    "#": "3", #(Hash/Three)
    "$": "4", #(Dollar/Four)
    "%": "5", #(Percent/Five)
    "^": "6", #(Caret/Six)
    "&": "7", #(Ampersand/Seven)
    "*": "8", #(Asterisk/Eight)
    "(": "9", #(Left Parenthesis/Nine)
    ")": "0", #(Right Parenthesis/Zero)
    "~": "`", #(Tilde/Backtick)
    "_": "-", #(Underscore/Hyphen)
    "+": "=", #(Plus/Equals)
    "{": "[", #(Left Curly/Square Bracket)
    "}": "]", #(Right Curly/Square Bracket)
    "|": "\\", #(Pipe/Backslash)
    ":": ";", #(Colon/Semicolon)
    '"': "'", #(Double Quote/Single Quote)
    "<": ",", #(Less Than/Comma)
    ">": ".", #(Greater Than/Period)
    "?": "/", #(Question Mark/Forward Slash)
}
#############AI HELP WORK ENDED HERE ############

KEYS = list(keyboardSymbols.keys())
VALUES = list(keyboardSymbols.values())

def decode(phrase,fromList,toList):
    # reverse the phrase
    output = phrase[::-1]
    for i in range(len(output)):
        sym_i = output[i]
        if sym_i in fromList:
            index_of_sym_i_in_fromList = fromList.index(sym_i)
            replacement_sym = toList[index_of_sym_i_in_fromList]
            output=output.replace(sym_i,replacement_sym)
    return output

def SecretPhraseDecrypter(SecretPhrase,DecryptAmount):
    """
    Docstring for SecretPhraseDecrypter
    
    :param SecretPhrase: The Secret Phrase You Want To Decrypt
    :param DecryptAmount: 1 means only decode, 2 means decode and then encode again
    :return: The Decrypted Phrase
    """

    print(f'Secrete phrase input = {SecretPhrase}')

    # decocde the phrase
    decrypted_phrase = decode(SecretPhrase,KEYS,VALUES)
    print(f'Decrypted phrase = {decrypted_phrase}')
    # # reverse it 
    # decrypted_phrase=SecretPhrase[::-1]
    # # and replace the keyboard symbols in it with their corresponding symbols
    # for i in range(len(decrypted_phrase)):
    #     sym_i = decrypted_phrase[i]
    #     if sym_i in VALUES:
    #         index_of_sym_i_in_VALUES = VALUES.index(sym_i)
    #         replacement_sym = KEYS[index_of_sym_i_in_VALUES]
    #         decrypted_phrase=decrypted_phrase.replace(sym_i,replacement_sym)
    # print(f'Decrypted phrase = {decrypted_phrase}')

    if DecryptAmount == 2:
        # then also encode the phrase again
        encrypted_phrase = decode(decrypted_phrase,VALUES,KEYS)
        print(f'Encrypted phrase = {encrypted_phrase}')
        # # first reverse it again
        # encrypted_phrase= decrypted_phrase[::-1]
        # # and replace the keyboard symbols with their corresponding symbols
        # for i in range(len(encrypted_phrase)):
        #     sym_i = encrypted_phrase[i]
        #     if sym_i in KEYS:
        #         index_of_sym_i_in_KEYS = KEYS.index(sym_i)
        #         replacement_sym = VALUES[index_of_sym_i_in_KEYS]
        #         encrypted_phrase=encrypted_phrase.replace(sym_i,replacement_sym)
        # print(f'Encrypted phrase = {encrypted_phrase}')

    return decrypted_phrase
    """
    How to use user will put encrypted phrase (String of text) And amount of cyphers (1 or 2)
    Your job is to decrypt it!
    Good Luck You'll Need It!
    """
#PUT TESTS HERE
def tests():
    # Finish The Code To Unlock The Tests!
    """
    Tests Go Here:
    """
    plain1 = "My cool cy111"
    code1 = "!!!yc looc yM"
    assert(SecretPhraseDecrypter(code1,2) == plain1)


if __name__ == "__main__":
    tests()
    
    code= "WH D# YM STAHT EDUD"
    answer=SecretPhraseDecrypter(code,1)
 


