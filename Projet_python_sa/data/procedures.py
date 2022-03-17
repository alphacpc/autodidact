from connectDB import conn, cursor;

cursor.execute("""
DELIMITER |

CREATE PROCEDURE getAllStudents()

BEGIN
    
    SELECT * FROM Students;

END|

DELIMITER ;

""")


cursor.execute("""
DELIMITER |

CREATE PROCEDURE getAllNotes()

BEGIN
    
    SELECT * FROM Notes;

END|

DELIMITER ;

""")

cursor.execute("""
DELIMITER |

CREATE PROCEDURE getSingleNotes()

BEGIN
    
    SELECT * FROM Notes WHERE numero = "BH54JJ6";

END|

DELIMITER ;

""")

conn.commit

print("Working well")