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
    
    with pytest.raises(ValueError, match="The book is already borrowed"):
        book1.borrow()

@pytest.mark.unit
def test_return_book():
    book1 = book.Book('Orgullo y prejuicio', 'Tenoch M.', 2026, 'ISBN001')
    assert book1.title == "Orgullo y prejuicio"
    book1.borrow()
    assert book1.borrowed == True
    
    book1.return_book()
    assert book1.borrowed == False

@pytest.fixture
def lib_init():
    lib = library.Library()
    book_tenoch = book.Book('Orgullo y prejuicio', 'Tenoch M.', 2026, 'ISBN001')
    lib.add_book(book_tenoch)
    
    # El ID debe coincidir con el que piden las pruebas ('ID0001')
    user_tenoch = user.User('Tenoch', 'ID0001')
    lib.add_user(user_tenoch)
    
    return lib  # ¡Faltaba retornar la librería inicializada!

@pytest.mark.system
def test_library_init(lib_init):
    lib = lib_init
    lib.borrow_book('ID0001', 'ISBN001')
    assert lib.books[0].borrowed == True

@pytest.mark.wip
def test_library_init_ID_NOT_REGISTER(lib_init):
    lib = lib_init
    
    with pytest.raises(ValueError, match='User not found'):
        lib.borrow_book('ID0003', 'ISBN001')

@pytest.mark.system
def test_system_full_cycle_borrow_return():
    # PS-01: Ciclo completo de préstamo y devolución
    lib = library.Library()
    
    # Registramos el libro y el usuario
    book_1984 = book.Book('1984', 'George Orwell', 1949, 'ISBN001')
    user_1 = user.User('Juan', 'ID0001')
    
    lib.add_book(book_1984)
    lib.add_user(user_1)
    
    # 1. El usuario pide prestado el libro
    lib.borrow_book('ID0001', 'ISBN001')
    assert lib.books[0].borrowed == True
    
    # 2. El usuario devuelve el libro (cumpliendo el RF5)
    # Nota: Si tu método return_book en la clase Library solo requiere el ISBN,
    # puedes dejarlo como lib.return_book('ISBN001')
    lib.return_book('ID0001', 'ISBN001') 
    
    # Verificamos que el libro esté disponible nuevamente
    assert lib.books[0].borrowed == False

@pytest.mark.system
def test_system_borrow_rejected_for_borrowed_book():
    # PS-02: Rechazo de préstamo de un libro que ya está prestado (RF4)
    lib = library.Library()
    
    # Registramos un libro y DOS usuarios diferentes
    book_moby = book.Book('Moby Dick', 'Herman Melville', 1851, 'ISBN004')
    user_1 = user.User('Ana', 'ID0001')
    user_2 = user.User('Luis', 'ID0002')
    
    lib.add_book(book_moby)
    lib.add_user(user_1)
    lib.add_user(user_2)
    
    # 1. El primer usuario (Ana) pide el libro con éxito
    lib.borrow_book('ID0001', 'ISBN004')
    assert lib.books[0].borrowed == True
    
    # 2. El segundo usuario (Luis) intenta pedir el MISMO libro
    # El sistema debe rechazarlo lanzando el ValueError
    with pytest.raises(ValueError, match="The book is already borrowed"):
        lib.borrow_book('ID0002', 'ISBN004')