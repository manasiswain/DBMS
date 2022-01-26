INSERT INTO RECEPTIONIST
VALUES(1, '9438473238', 'r_address1', 'receptionist1'),
    (2, '9342147383', 'r_address2', 'receptionist2'),
    (3, '8342227993', 'r_address3', 'receptionist3'),
    (4, '9342221193', 'r_address4', 'receptionist4'),
    (5, '8342227923', 'r_address5', 'receptionist5'),
    (6, '9333237993', 'r_address6', 'receptionist6'),
    (7, '8134227993', 'r_address7', 'receptionist7'),
    (8, '9942227993', 'r_address8', 'receptionist8');

INSERT INTO DONOR
VALUES ('d_person1', 1, 'd_address1', 21, '9443847383', 'M', 1),
    ('d_person2', 2, 'd_address2', 22, '9443847384', 'F', 1),
    ('d_person3', 3, 'd_address3', 23, '9443847385', 'M', 2),
    ('d_person4', 4, 'd_address4', 24, '9443847386', 'F', 1),
    ('d_person5', 5, 'd_address5', 25, '9443847387', 'M', 3),
    ('d_person6', 6, 'd_address6', 26, '9443847388', 'F', 2),
    ('d_person7', 7, 'd_address7', 27, '9443847389', 'F', 1),
    ('d_person8', 8, 'd_address8', 28, '9443847381', 'F', 2),
    ('d_person9', 9, 'd_address9', 29, '9443847382', 'M', 3),
    ('d_person10',10, 'd_address10',30,'9443847380', 'F', 1);

INSERT INTO BLOOD_BANK
VALUES (100,1234,1),
    (50,3241,3),
    (70,1204,2),
    (50,1004,4),
    (150,1203,1),
    (200,1209,5),
    (80,1207,7),
    (78,1765,1),
    (20,1223,3),
    (10,1907,3);

INSERT INTO BLOOD
VALUES (500, 'ABCA', 'O+', 1, 1234),
    (450, 'ABCB', 'AB+',2, 1234),
    (300, 'ABCC', 'B+' ,3, 3241),
    (700, 'ABCD', 'AB-',4, 1234),
    (450, 'ABCE', 'O-', 5, 1234),
    (465, 'ABCF', 'A+', 6, 1004),
    (500, 'ABCG', 'A+', 7, 3241),
    (275, 'ABCH', 'O+', 8, 1907),
    (305, 'ABCI', 'A+', 9, 1907),
    (90,  'ABCJ', 'AB+',10,3241);

INSERT INTO HOSPITALS
VALUES('Hospital1','h_address1','9785646952'),
    ('Hospital2','h_address2','8885246912'),
    ('Hospital3','h_address3','9335636922'),
    ('Hospital4','h_address4','9335632212'),
    ('Hospital5','h_address5','9335636762'),
    ('Hospital6','h_address6','9335645922'),
    ('Hospital7','h_address7','9388636922'),
    ('Hospital8','h_address8','9399936922');
INSERT INTO PATIENT
VALUES('p_person1', 1, 'p_address1', 10, '9843847383', 'M', 'Hospital1'),
    ('p_person2', 2, 'p_address2', 20, '9143847384', 'M', 'Hospital2'),
    ('p_person3', 3, 'p_address3', 2,  '9233847385', 'F', 'Hospital2'),
    ('p_person4', 4, 'p_address4', 27, '9343821386', 'F', 'Hospital3'),
    ('p_person5', 5, 'p_address5', 10, '9224384737', 'M','Hospital4'),
    ('p_person6', 6, 'p_address6', 27, '9454647388', 'M', 'Hospital6'),
    ('p_person7', 7, 'p_address7', 25, '9897847389', 'F', 'Hospital5'),
    ('p_person8', 8, 'p_address8', 50, '9333847381', 'F', 'Hospital8'),
    ('p_person9', 9, 'p_address9', 79, '9443876682', 'M', 'Hospital8'),
    ('p_person10',10,'p_address10',90,'9465237380', 'F', 'Hospital1');
INSERT INTO BLOOD_BANK_MANAGER
VALUES(1,'person1@gmail.com','9843847383','m_person1',1234),
    (2,'person2@gmail.com','9143847384','m_person2',3241),
    (3,'person3@gmail.com','9233847385','m_person3',1204),
    (4,'person4@gmail.com','9343821386','m_person4',1004),
    (5,'person5@gmail.com','9224384737','m_person5',1203),
    (6,'person6@gmail.com','9843847113','m_person6',1209),
    (7,'person7@gmail.com','9143822384','m_person7',1207),
    (8,'person8@gmail.com','9233547385','m_person8',1765),
    (9,'person9@gmail.com','9433266386','m_person9',1223),
    (10,'person10@gmail.com','9224548477','m_person10',1907);
INSERT INTO ORDERS
VALUES('Hospital1',1234),
    ('Hospital2',1203),
    ('Hospital3',1203),
    ('Hospital2',1234),
    ('Hospital6',3241),
    ('Hospital5',3241),
    ('Hospital1',1203),
    ('Hospital7',1204);
INSERT INTO STOCK
VALUES(1,20,'desc1',1234),
    (2,35,'desc2',1203),
    (3,100,'desc3',1204),
    (4,89,'desc4',1234),
    (5,97,'desc5',3241),
    (6,32,'desc6',3241),
    (7,22,'desc7',1004),
    (8,21,'desc8',1004);
