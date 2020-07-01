import re


def is_stressful(subj):
    """
        recognize stressful subject
    """
    # temp = subj.lower()
    # help = ''
    # help_list = list('help')
    # asap = ''
    # asap_list = list('asap')
    # urgent = ''
    # urgent_list = list('urgent')
    # if 'help' in temp or 'asap' in temp or 'urgent' in temp:
    #     return True
    # for ch in temp:
    #     if ch in help_list:
    #         help += ch
    #     if ch in asap_list:
    #         asap += ch
    #     if ch in urgent_list:
    #         urgent += ch
    # if help == 'help':
    #     return True
    # if asap == 'asap':
    #     return True
    # if urgent == 'urgent':
    #     return True
    # return False
    re_pattren = r'help|asap|urgent|!!!|h.*e.*l.*p.*|a.*s.*a.*p.*|u.*r.*g.*e.*n.*t.*'
    re_mo = re.search(re_pattren, subj.lower())
    if re_mo:
        return True
    return False


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("Heeeeeey!!! I’m having so much fun!”") == True
    print('Done! Go Check it!')
