import string
from typing import List


# OPTIUNEA 1 \/ \/ \/
def citire_lista():
    lst = []
    given_string = input("Dati sirurile separate prin virgula: ")
    list_as_string = given_string.split(",")
    for x in list_as_string:
        lst.append(str(x))
    return lst
# OPTIUNEA 1 /\ /\ /\


# OPTIUNEA 2 \/ \/ \/
def is_found_in_list(lst: List[str], string_from_keyboard: str) -> bool:
    """
    Determina daca un sir de caractere citit de la tastatura se gaseste in lista
    :param lst: lista care contine siruri de caractere
    :param string_from_keyboard: sir de caractere
    :return: True daca sirul citit de la tastatura se afla in lista, False in caz contrar
    """
    for string_from_list in lst:
        if string_from_keyboard == string_from_list:
            return True
    return False


def test_is_found_in_list():
    assert is_found_in_list([], "aaa") is False
    assert is_found_in_list(["aaa", "bbb", "cmtc", "drd", "aaa"], "aaa") is True
    assert is_found_in_list(["aaa", "bbb", "cmtc", "drd", "aaa"], "abc") is False
# OPTIUNEA 2 /\ /\ /\


# OPTIUNEA 3 \/ \/ \/
def is_list_unique(lst: List[str]) -> List[str]:
    """
    Determina daca doua siruri de caractere se repeta in lista
    :param lst: lista care contine siruri de caractere
    :return: lista cu sirurile de caractere care se repeta
    """
    duplicates_from_list = []
    for i in range(len(lst)):
        for x in lst[i+1:]:
            if lst[i] == x:
                duplicates_from_list.append(lst[i])
    return duplicates_from_list


def test_is_list_unique():
    assert is_list_unique(["aaa", "bbb", "cmtc", "drd", "aaa"]) == ["aaa"]
    assert is_list_unique(["aaa", "bbb", "cmtc", "drd", "aaa", "drd"]) == ["aaa", "drd"]
    assert is_list_unique(["aaa", "bbb", "cmtc", "drd"]) == []
# OPTIUNEA 3 /\ /\ /\


# OPTIUNEA 4 \/ \/ \/
def is_palindrome(string_from_list: str) -> bool:
    """
    Determina daca un sir de caractere dat este palindrom
    :param string_from_list: sir de caractere
    :return: True daca sirul de caractere dat este palindrom, False in caz contrar
    """
    inverted_string_from_list = string_from_list[::-1]
    if string_from_list == inverted_string_from_list:
        return True
    return False


def test_is_palindrome():
    assert is_palindrome("aaa") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("") is True
    assert is_palindrome("acba") is False
    assert is_palindrome("abadaba") is True
    assert is_palindrome("abadba") is False


def is_duplicate(palindromes_list: List[str], string_from_list: str) -> bool:
    """
    Determina daca un sir de caractere se repeta intr-o lista
    :param palindromes_list: lista care contine siruri de caractere
    :param string_from_list: sir de caractere
    :return: True daca un sir de caractere se repeta intr-o lista, False in caz contrar
    """
    for string_from_palindromes_list in palindromes_list:
        if string_from_list == string_from_palindromes_list:
            return True
    return False


def test_is_duplicate():
    assert is_duplicate(["aaa", "bbb", "cmtc", "drd", "aaa"], "aaa") is True
    assert is_duplicate(["bbb", "cmtc", "drd"], "aaa") is False
    assert is_duplicate([], "aaa") is False


def select_palindromes_from_list(lst: List[str]) -> List[str]:
    """
    Determina daca exista siruri de caractere de tip palindrom in lista
    :param lst: lista care contine siruri de caractere
    :return: lista cu sirurile de caractere de tip palindrom
    """
    palindromes_from_list = []
    for string_from_list in lst:
        if is_duplicate(palindromes_from_list, string_from_list) is False and is_palindrome(string_from_list) is True:
            palindromes_from_list.append(string_from_list)
    return palindromes_from_list


def test_select_palindromes_from_list():
    assert select_palindromes_from_list(["ada", "abc", "cmtc", "drd", "aaa"]) == ["ada", "drd", "aaa"]
    assert select_palindromes_from_list(["abc", "cmtc", "brbr"]) == []
    assert select_palindromes_from_list([]) == []
# OPTIUNEA 4 /\ /\ /\


# OPTIUNEA 5 \/ \/ \/
def count_appearances_of_char(lst: List[str], character: str) -> int:
    """
    Determina de cate ori apare un caracter intr-o lista
    :param lst: lista care contine siruri de caractere
    :param character: o litera mica de la a la z
    :return: numarul de aparitii a caracterului in lista
    """
    number_of_appearances = 0
    for string_from_list in lst:
        number_of_appearances = number_of_appearances + string_from_list.count(character)
    return number_of_appearances


def test_count_appearances_of_char():
    assert count_appearances_of_char(["aaa", "bbab", "caamtc", "drd", "aaa"], 'a') == 9
    assert count_appearances_of_char(["aaa", "bbb", "cmtc", "drd", "aaa"], 'b') == 3
    assert count_appearances_of_char(["aaa", "bbb", "cmtc", "drd", "aaa", "drd"], 'c') == 2


def change_from_string_to_maximum(lst: List[str]) -> List[int and str]:
    """
    Determina si inlocuieste sirurile care contin caracterul care apare de cele mai
    multe ori în toata lista cu numarul de aparitii ale acestui caracter
    :param lst: lista care contine siruri de caractere
    :return: lista obtinuta prin inlocuirea sirurilor care contin caracterul care
             apare de cele mai multe ori în toata lista cu numarul de aparitii ale
             acestui caracter
    """
    changed_string = lst[:]
    alphabet_lowercase = string.ascii_lowercase
    maximum_appearances = 0
    maximum_letter = None
    for letter_from_alphabet_lowercase in alphabet_lowercase:
        if count_appearances_of_char(lst, letter_from_alphabet_lowercase) > maximum_appearances:
            maximum_appearances = count_appearances_of_char(lst, letter_from_alphabet_lowercase)
            maximum_letter = letter_from_alphabet_lowercase
    for i in range(len(changed_string)):
        if changed_string[i].count(maximum_letter):
            changed_string[i] = maximum_appearances
    return changed_string


def test_change_from_string_to_maximum():
    assert change_from_string_to_maximum(["aaa", "bbab", "caamtc", "drd", "aaa"]) == [9, 9, 9, "drd", 9]
    assert change_from_string_to_maximum(["aaa", "bbb", "cmtc", "drd", "aaa", "drd"]) == [6, "bbb", "cmtc", "drd", 6, "drd"]
    assert change_from_string_to_maximum(["aba", "bbb", "cmtc", "drd", "aba", "bac", "zax", "zfb"]) == [7, 7, "cmtc", "drd", 7, 7, "zax", 7]
# OPTIUNEA 5 /\ /\ /\


def print_menu():
    print("1. Citire lista.")
    print("2. Determina si afiseaza DA daca un sir de caractere citit de la "
          "tastatura se gaseste in lista sau NU in caz contrar.")
    print("3. Determina si afiseaza o lista cu toate sirurile de caractere "
          "care se repeta in lista, sau UNIC daca nu exista niciun sir de "
          "acest gen.")
    print("4. Determina si afiseaza toate sirurile de caractere din lista care sunt de tip palindrom.")
    print("5. Determina si afiseaza lista obtinuta prin inlocuirea sirurilor care contin caracterul "
          "care apare de cele mai multe ori în toata lista cu numarul de aparitii ale acestui caracter")
    print("A. Afisare lista")
    print("6. Iesire")


def main():
    should_run = True
    lst = []
    while should_run:
        print_menu()
        optiune = input("Selectati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            string_from_keyboard = input("Sirul citit de la tastatura: ")
            if is_found_in_list(lst, string_from_keyboard) is True:
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            if is_list_unique(lst):
                print(is_list_unique(lst))
            else:
                print("UNIC")
        elif optiune == "4":
            if not select_palindromes_from_list(lst):
                print("Nu exista siruri de caractere de tip palindrom!")
            else:
                print(select_palindromes_from_list(lst))
        elif optiune == "5":
            print(change_from_string_to_maximum(lst))
        elif optiune == "A":
            print(lst)
        elif optiune == "6":
            should_run = False
        else:
            print("Optiune gresita! Reincercati!")


if __name__ == "__main__":
    test_is_found_in_list()
    test_is_list_unique()
    test_is_palindrome()
    test_is_duplicate()
    test_select_palindromes_from_list()
    test_count_appearances_of_char()
    test_change_from_string_to_maximum()
    main()
