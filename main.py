from typing import List


# OPTIUNEA 1 \/ \/ \/
def citire_lista():
    lst = []
    given_string = input("Dati elementele separate prin virgula: ")
    number_as_string = given_string.split(",")
    for x in number_as_string:
        lst.append(float(x))
    return lst
# OPTIUNEA 1 /\ /\ /\


# OPTIUNEA 2 \/ \/ \/
def all_integers_from_list(lst: List[float]) -> List[float]:
    """
    Determina toate elementele intregi dintr-o lista
    :param lst: lista cu numere reale
    :return: toate elementele intregi dintr-o lista
    """
    result = []
    for x in lst:
        if x % 1 == 0:
            result.append(int(x))
    return result


def test_all_integers_from_list():
    assert all_integers_from_list([4.5, 2.3]) == []
    assert all_integers_from_list([1.0, 9.8, 7.0]) == [1.0, 7.0]
# OPTIUNEA 2 /\ /\ /\


# OPTIUNEA 3 \/ \/ \/
def max_div_k(lst: List[float], k: int) -> float:
    """
    Determina cel mai mare numar din lista divizibil cu k
    :param lst: lista cu numere reale
    :param k: numar intreg
    :return: Cel mai mare numar din lista divizibil cu k
    """
    nr_ordonate = lst[:]
    nr_ordonate.sort(reverse=True)
    for x in nr_ordonate:
        if x % k == 0:
            return x


def test_max_div_k():
    assert max_div_k([4.5, 6.0, 7.0], 4) is None
    assert max_div_k([6.0, 8.0, 9.9], 3) == 6.0
    assert max_div_k([8.0, 4.5, 10.0, 5.41, 2.3, 6.0], 2) == 10.0
# OPTIUNEA 3 /\ /\ /\


# OPTIUNEA 4 \/ \/ \/
def is_float_palindrome(lst: List[float]) -> List[float]:
    """
    Determina toate valorile ale caror parte fractionara este palindrom
    :param lst: lista cu numere reale
    :return: valorile ale caror parte fractionara este palindrom
    """
    result_float_palindrom = []
    for x in lst:
        x_str = str(x)
        fractional_part = x_str.split(".")[1]
        # fractional_part[::-1] este fractional_part inversat (ex.: "123" => "321")
        if fractional_part == fractional_part[::-1]:
            result_float_palindrom.append(x)
    return result_float_palindrom


def test_is_float_palindrome():
    assert is_float_palindrome([2.211, 3.45]) == []
    assert is_float_palindrome([5.0, 6.45, 3.1, 2.343]) == [5.0, 3.1, 2.343]
# OPTIUNEA 4 /\ /\ /\


# OPTIUNEA 5 \/ \/ \/
def is_prime(x: int) -> bool:
    """
    Determina daca un numar dat este prim sau nu
    :param x: numar intreg
    :return: True daca numarul este prim, False in caz contrar
    """
    if x < 2:
        return False
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False


def processed_list(lst: List[float]) -> List[str]:
    """
    Determina lista obtinuta din lista initiala in care float-urile cu partea intreaga
    a radicalului numar prim sunt puse ca string-uri cu caracterele in ordine inversa
    :param lst: lista cu numere reale
    :return: lista obtinuta din lista initiala in care float-urile cu partea intreaga
             a radicalului numar prim sunt puse ca string-uri cu caracterele in ordine
             inversa
    """
    final_list = []
    for x in lst:
        integer_part_from_sqrt = int(x ** 0.5)
        if is_prime(integer_part_from_sqrt):
            final_list.append(str(x)[::-1])
        else:
            final_list.append(x)
    return final_list


def test_processed_list():
    assert processed_list([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]
# OPTIUNEA 5 /\ /\ /\


def print_menu():
    print("1. Citire lista cu numere reale.")
    print("2. Determina si afiseaza toate numerele intregi din lista.")
    print("3. Determina si afiseaza cel mai mare numar divizibil cu un numar citit de la tastatura")
    print("4. Determina si afiseaza toate floaturile ale caror parte fractionara este palindrom")
    print("5. Determina si afiseaza lista obtinuta din lista initiala in care float-urile cu partea "
          "intreaga a radicalului numar prim sunt puse ca string-uri cu caracterele in ordine inversa")
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
            print("Elementele intregi din lista sunt: ", all_integers_from_list(lst))
        elif optiune == "3":
            k = int(input("Dati o valoare pentru k: "))
            print("Cel mai mare element divizibil cu", k, "este: ", max_div_k(lst, k))
        elif optiune == "4":
            print("Elementele ale caror parte fractionara este palindrom sunt: ", is_float_palindrome(lst))
        elif optiune == "5":
            print("Lista procesata este: ", processed_list(lst))
        elif optiune == "A":
            print(lst)
        elif optiune == "6":
            should_run = False
        else:
            print("Optiune gresita! Reincercati!")


if __name__ == "__main__":
    test_all_integers_from_list()
    test_max_div_k()
    test_is_float_palindrome()
    test_is_prime()
    test_processed_list()
    main()
