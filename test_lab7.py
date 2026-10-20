import book
import pytest
import library
import user

@pytest.mark.unit
def test_borrow_book():

    book1 = book.Book('Orgullo y prejuicio', 'Tenoch M.', 2026, 'ISBN001')

    assert book1.title == "Orgullo y prejuicio"

    book1.borrow()

    assert book1.borrowed == True

@pytest.mark.wip
def test_borrow_two_times():

    book1 = book.Book('Orgullo y prejuicio', 'Tenoch M.', 2026, 'ISBN001')

    assert book1.title == "Orgullo y prejuicio"

    book1.borrow()

    assert book1.borrowed == True
    with pytest.raises(ValueError, match = "The book is already borrow"):
        book1.borrow()

@pytest.mark.unit
def test_return_book():

    book1 = book.Book('Orgullo y prejuicio', 'Tenoch M.', 2026, 'ISBN001')

    assert book1.title == "Orgullo y prejuicio"

    book1.borrow()

    assert book1.borrowed == True
    book1.return_book()
    assert boo1.borrowed == False

@pytest.mark.wip
def test_borrow_and_try_Exept():

    book1 = book.Book('Orgullo y prejuicio', 'Tenoch M.', 2026, 'ISBN001')

    assert book1.title == "Orgullo y prejuicio"

    book1.borrow()

    assert book1.borrowed == True
    with pytest.raises(ValueError, match = "The book is already borrowed"):
        book1.borrow()

@pytest.fixture
def lib_init():
    lib = library.Library()
    book_tenoch =  book.Book('Orgullo y prejuicio', 'Tenoch M.', 2026, 'ISBN001')
    lib.add_book(book_tenoch)
    Tenich = user.User('Tenoch','00001')
    lib.add_user(Tenich)

@pytest.mak.system
def test_library_init(lib_init):
    lib = lib_init
    lib.borrow_book('ID0001', 'ISBN001')

    assert lib.books[0].borrowed == True

@pytest.mak.wipwwwdd
def test_library_init_ID_NOT_REGISTER(lib_init):
    lib = lib_init
    
    with pytest.raises(ValueError, march = 'User not found'):
        lib.borrow_book('ID0003', 'ISBN001')