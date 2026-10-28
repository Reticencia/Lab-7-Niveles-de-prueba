import pytest
# Asegúrate de importar tus clases desde el archivo correspondiente, por ejemplo:
# from library import Book, User, Library

# ==========================================
# Actividad 1: Pruebas Unitarias (PU)[cite: 3, 4]
# ==========================================

def test_pu_01_borrow_book():
    """PU-01: Instanciar book1 y ejecutar book1.borrow()"""
    book1 = Book('1984', 'George Orwell', 1949, 'ISBN001')
    book1.borrow()
    assert book1.borrowed is True

def test_pu_02_borrow_already_borrowed():
    """PU-02: Ejecutar book1.borrow() en un libro que ya tiene el estado borrowed = True"""
    book1 = Book('1984', 'George Orwell', 1949, 'ISBN001')
    book1.borrow()
    with pytest.raises(ValueError, match="The book is already borrowed"):
        book1.borrow()

def test_pu_03_return_book():
    """PU-03: Ejecutar book1.return_book() en un libro prestado"""
    book1 = Book('1984', 'George Orwell', 1949, 'ISBN001')
    book1.borrow()
    book1.return_book()
    assert book1.borrowed is False

def test_pu_04_book_instantiation():
    """PU-04: Instanciar un libro específico y verificar el título"""
    book1 = Book('Orgullo y prejuicio', 'Tenoch M.', 2026, 'ISBN001')
    assert book1.title == 'Orgullo y prejuicio'


# ==========================================
# Actividad 2: Pruebas de Integración (PI)[cite: 4, 5]
# ==========================================

def test_pi_01_library_borrow_updates_book_state():
    """PI-01: Agregar libro y usuario, y realizar un préstamo exitoso"""
    lib = Library()
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    user = User('ID0001', 'Juan')
    
    lib.add_book(book)
    lib.add_user(user)
    lib.borrow_book('ID0001', 'ISBN001')
    
    # La clase Library actualiza el estado del libro de la clase Book a prestado
    assert book.borrowed is True

def test_pi_02_library_borrow_user_not_found():
    """PI-02: Solicitar préstamo con usuario no registrado"""
    lib = Library()
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    lib.add_book(book)
    
    with pytest.raises(ValueError, match="User not found"):
        lib.borrow_book('ID0003', 'ISBN001')


# ==========================================
# Actividad 3: Pruebas de Sistema (PS)[cite: 5, 6]
# ==========================================

def test_ps_01_system_full_cycle_borrow_return():
    """PS-01: Ciclo completo de registro, préstamo y devolución"""
    lib = Library()
    book = Book('1984', 'George Orwell', 1949, 'ISBN001')
    user = User('ID0001', 'Juan')
    
    # 1 y 2. Registrar libro y usuario
    lib.add_book(book)
    lib.add_user(user)
    
    # 3. Préstamo del libro al usuario
    lib.borrow_book('ID0001', 'ISBN001')
    assert book.borrowed is True
    
    # 4. Devolución del libro
    book.return_book()
    
    # El libro finaliza con estado disponible
    assert book.borrowed is False

def test_ps_02_system_borrow_rejected_for_borrowed_book():
    """PS-02: Intento de préstamo múltiple del mismo libro"""
    lib = Library()
    book = Book('Moby Dick', 'Herman Melville', 1851, 'ISBN004')
    user1 = User('ID0001', 'Juan')
    user2 = User('ID0002', 'Maria')
    
    # 1 y 2. Registrar libro y usuarios
    lib.add_book(book)
    lib.add_user(user1)
    lib.add_user(user2)
    
    # 3. "ID0001" pide prestado el libro
    lib.borrow_book('ID0001', 'ISBN004')
    
    # 4. "ID0002" intenta pedir el mismo libro y el sistema lo rechaza
    with pytest.raises(ValueError, match="The book is already borrowed"):
        lib.borrow_book('ID0002', 'ISBN004')