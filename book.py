import pytest
from book import Book, CONFIG
# from library import User, Library  # Asegúrate de importar tus otras clases

# ==========================================
# Pruebas Unitarias (Clase Book)
# ==========================================

def test_borrow_book():
    """Prueba que un libro cambia su estado a prestado correctamente."""
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    book.borrow()
    assert book.borrowed is True

def test_borrow_two_times_book():
    """Prueba que el método borrow() lance ValueError si ya está prestado."""
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    book.borrow()
    
    with pytest.raises(ValueError, match="The book is already borrowed"):
        book.borrow()

def test_return_book():
    """Prueba la devolución exitosa de un libro prestado."""
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    book.borrow()  # Se debe prestar primero según tu nueva lógica
    book.return_book()
    assert book.borrowed is False

def test_return_unborrowed_book_raises_error():
    """Prueba que no se pueda devolver un libro que no ha sido prestado."""
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    with pytest.raises(ValueError, match="The book is not currently borrowed"):
        book.return_book()

def test_borrow_and_try_Except():
    """Prueba el método safe_borrow cuando el libro ya está prestado."""
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    book.borrow() # Lo prestamos para forzar el error
    
    resultado = book.safe_borrow()
    assert resultado == "Error: The book is already borrowed"

def test_safe_borrow_success():
    """Prueba el método safe_borrow cuando el libro está disponible."""
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    resultado = book.safe_borrow()
    assert resultado == "OK"
    assert book.borrowed is True

def test_loan_days():
    """Prueba la lectura correcta del diccionario CONFIG global."""
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    assert book.loan_days() == 14

def test_loan_days_monkeypatch(monkeypatch):
    """(Opcional) Prueba modificando la constante dinámicamente usando pytest."""
    monkeypatch.setitem(CONFIG, "loan_days", 7)
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    assert book.loan_days() == 7