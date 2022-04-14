/* INSERT DATA INTO `Appointments` TABLE */
INSERT INTO Appointments (app_id, blood_pressure, height, notes, patient_id, room_number, temperature, weight) VALUES
(1, '112/61', 55.7, DEFAULT, 4, 10, 96.8, 242.26),
(2, '104/72', 71.87, DEFAULT, 4, 11, 99.01, 152.92),
(3, '112/90', 71.37, DEFAULT, 1, 12, 96.45, 183.5),
(4, '81/89', 63.15, 'Key beat drop step child this degree. Baby interview senior stop always Congress majority campaign. Various floor itself news experience.', 2, 2, 105.17, 233.45),
(5, '105/78', 65.42, DEFAULT, 3, 17, 100.62, 326.56);
/* INSERT DATA INTO `ArchivedFiles` TABLE */
INSERT INTO ArchivedFiles (emp_id, file_blob, file_id, file_name, patient_id) VALUES
(1, DEFAULT, 1, 'up.txt', 5),
(2, DEFAULT, 2, 'make.wav', 4),
(4, DEFAULT, 3, 'card.pages', 4),
(2, DEFAULT, 4, 'generation.mov', 1),
(4, DEFAULT, 5, 'matter.mp3', 1);
/* INSERT DATA INTO `BloodExam` TABLE */
INSERT INTO BloodExam (blood_sugar, blood_type, exam_id) VALUES
(82, 'B+', 1),
(72, 'B-', 3);
/* INSERT DATA INTO `ConductedBys` TABLE */
INSERT INTO ConductedBys (lab_id, report_id) VALUES
(4, 1),
(5, 2),
(4, 3),
(4, 4),
(3, 5);
/* INSERT DATA INTO `CoveredBys` TABLE */
INSERT INTO CoveredBys (group_number, member_id, patient_id, policy_holder_name, provider_id) VALUES
('843318', 'LHV886016419', 2, 'Amanda Zavala', 3),
('590262', 'RQK535749220', 2, 'Amanda Zavala', 1),
('599271', 'HYM812379332', 1, 'Thomas Moon', 1),
('778514', 'RUF089577403', 4, 'John Carlson', 3),
('357345', 'KXX963546030', 1, 'Thomas Moon', 3);
/* INSERT DATA INTO `CovidExams` TABLE */
INSERT INTO CovidExams (exam_id, is_positive, test_type) VALUES
(2, True, 'PCR'),
(4, False, 'PCR'),
(5, False, 'Antigen');
/* INSERT DATA INTO `Diagnoses` TABLE */
INSERT INTO Diagnoses (app_id, comment, emp_id, icd_code, patient_id) VALUES
(2, 'Pattern president add lead network the. Live teach movie I situation understand agree.', 3, 'A009', 4),
(2, 'Difficult there leg theory case north. Class on reach.', 3, 'A001', 4),
(3, 'Structure your those head. Page single theory. American focus something who blood. Certain hotel should.', 2, 'A000', 1),
(3, 'Huge away represent race sing nation network. Check clearly ahead career. Ground think save respond friend budget while.', 2, 'A009', 1),
(4, 'Recent project speech director city necessary thus sister. Tv collection still support these military part. Just raise enough onto try.', 3, 'A000', 2);
/* INSERT DATA INTO `EmpImmunizations` TABLE */
INSERT INTO EmpImmunizations (emp_id, immunization_id) VALUES
(4, 5),
(2, 4),
(5, 4),
(2, 4),
(5, 3);
/* INSERT DATA INTO `Employees` TABLE */
INSERT INTO Employees (address, birthday, dea_number, email, emp_id, gender, medical_license_number, name, phone_number, role, salary, ssn) VALUES
('027 Jonathon Estate Suite 878\nNorth Troyport, NH 07035', '2012-04-12', 'MG0300891', 'rgray@example.net', 1, 'Male', 'GP-2066', 'Sheri Burnett', '(466)109-3523', 'Physician General Practitioner', 255099, '896-54-0517'),
('24000 Erin Point Suite 590\nJosephmouth, NE 49318', '2013-02-26', 'BS5900422', 'hmarsh@example.com', 2, 'Male', 'RN-4555', 'Cassandra Bennett', '934-421-7610', 'Nurse', 63897, '137-84-8534'),
('71760 Rogers Spur Apt. 296\nNorth Lindseyborough, IN 08516', '2015-05-06', DEFAULT, 'kevin11@example.net', 3, 'Male', DEFAULT, 'Brent Hawkins', '568-241-7304x2814', 'Receptionist', 66661, '493-61-5523'),
('76430 Cindy Cove\nSouth Nicholas, FL 14230', '2014-08-01', 'BI0555082', 'brownmichelle@example.net', 4, 'Female', 'PA-5773', 'Victoria Hernandez MD', '001-361-534-9263', 'Physician Assistant', 126466, '029-68-7400'),
('Unit 8688 Box 0918\nDPO AP 10509', '2013-08-05', 'BK0024894', 'blakeshane@example.org', 5, 'Female', 'PA-7699', 'Susan Harris', '+1-269-471-1801x320', 'Physician Assistant', 121383, '820-20-7549');
/* INSERT DATA INTO `Exams` TABLE */
INSERT INTO Exams (app_id, comment, exam_id, report_id) VALUES
(4, 'Matter nice really listen meeting language condition. Fund indicate help north friend state do.', 1, 1),
(4, 'Simple improve language thousand need when simple. Involve education little direction exist.', 2, 5),
(2, DEFAULT, 3, 4),
(3, DEFAULT, 4, 2),
(4, DEFAULT, 5, 4);
/* INSERT DATA INTO `Experiencing` TABLE */
INSERT INTO Experiencing (app_id, comment, icd_code) VALUES
(1, DEFAULT, 'A009'),
(2, DEFAULT, 'A009'),
(3, DEFAULT, 'A000'),
(3, 'Company enter son foreign remember site military.', 'A001'),
(4, DEFAULT, 'A000'),
(4, 'One political almost serious stand author possible lead.', 'A001'),
(5, DEFAULT, 'A001');
/* INSERT DATA INTO `Immunizations` TABLE */
INSERT INTO Immunizations (immunization_id, immunization_type) VALUES
(1, 'Mumps'),
(2, 'Haemophilus Influenza Type B'),
(3, 'Tuberculosis'),
(4, 'Pertussis'),
(5, 'Tuberculosis');
/* INSERT DATA INTO `ImmunizedBys` TABLE */
INSERT INTO ImmunizedBys (immunization_id, patient_id) VALUES
(3, 4),
(2, 5),
(5, 2),
(3, 1),
(3, 3);
/* INSERT DATA INTO `InsuranceProviders` TABLE */
INSERT INTO InsuranceProviders (insurance_name, is_in_network, my_policy_number, provider_id) VALUES
('Snyder LLC', True, '46660', 0),
('Walls, Allen and Blair', True, '50076', 1),
('Wu-Guzman', True, '12560', 2),
('Hughes-Williams', True, '72009', 3),
('Soto Inc', True, '85367', 4);
/* INSERT DATA INTO `LabReports` TABLE */
INSERT INTO LabReports (app_id, file_id, icd_code, info, report_id, result_info) VALUES
(2, 5, 'A001', 'Few participant true lead. Long not improve begin.', 1, 'Father growth behind probably. Statement carry next according.'),
(3, 3, 'A009', 'Make real use nice themselves gas best above. Marriage worker ever across great.', 2, 'Back off difficult happen. Team certainly explain current simply process. Executive partner story budget great than.'),
(3, 4, 'A009', 'Trouble it grow husband short year term look. Building child usually sea upon.', 3, 'Body himself home message woman. Stock determine human find discussion military ability. First through dinner whose worker offer American.'),
(3, 3, 'A000', 'Rise condition Congress recognize agreement.', 4, 'Movement can start paper tree bank.'),
(1, 1, 'A001', 'Minute perform indeed.', 5, 'Dinner indeed listen a decision. Past especially old.');
/* INSERT DATA INTO `MedicalStaff` TABLE */
INSERT INTO MedicalStaff (app_id, emp_id) VALUES
(1, 2),
(1, 1),
(1, 4),
(2, 3),
(2, 5),
(2, 1),
(3, 2),
(4, 1),
(4, 4),
(4, 5),
(5, 1),
(5, 3);
/* INSERT DATA INTO `Patients` TABLE */
INSERT INTO Patients (address, birthday, email, gender, name, patient_id, phone_number, ssn) VALUES
('578 Michael Island\nNew Thomas, NC 34644', '2010-11-11', 'montgomeryjohn@example.net', 'Male', 'Thomas Moon', 1, '(604)876-4759x3824', '723-78-2408'),
('583 Wallace Ranch\nStewartbury, HI 25324', '2010-01-13', 'kaisernancy@example.com', 'Male', 'Amanda Zavala', 2, '(097)535-1393x3287', '112-39-9032'),
('59179 Bruce Gardens Apt. 413\nLauramouth, AR 13687', '2012-06-28', 'pattylawrence@example.com', 'Genderfluid', 'Savannah Robinson', 3, '122-018-6848', '594-36-7383'),
('086 Mary Cliff\nNorth Deborah, NE 24135', '2018-10-14', 'leetara@example.net', 'Female', 'John Carlson', 4, '+1-891-013-9916x1510', '127-62-3451'),
('564 Ann Bridge Suite 150\nDennisfort, RI 38233', '2018-08-21', 'awade@example.com', 'Genderfluid', 'Leslie Mcclain', 5, '(345)792-3022x5841', '698-53-9325');
/* INSERT DATA INTO `Pharmacies` TABLE */
INSERT INTO Pharmacies (pharmacy_address, pharmacy_name) VALUES
('3407 Smith Hills\nPort Tiffanyport, PA 20977', 'Mccarthy-Ruiz'),
('640 Joseph Skyway\nNorth Jonathanhaven, OR 93557', 'Wallace-Francis'),
('101 Torres Junctions\nNew Micheleburgh, MT 38471', 'Meyer-Berry'),
('8644 Watson Road\nEast David, MS 53089', 'Mcdonald, Castro and Evans'),
('77857 Scott Divide Suite 093\nWest Thomastown, NC 09211', 'Camacho, Parks and Harmon');
/* INSERT DATA INTO `Prescriptions` TABLE */
INSERT INTO Prescriptions (drug_name, emp_id, instructions, patient_id, pharmacy_address, prescription_date, prescription_id, quantity, refills) VALUES
('Park, Hickman and Cooley', 3, 'Break word source wall drug. Race government trouble tonight former section across. North weight guy. Fall manager idea issue color small notice kind.', 4, '8644 Watson Road\nEast David, MS 53089', '2014-04-16', 1, 54, 5),
('Fry Group', 3, DEFAULT, 1, '101 Torres Junctions\nNew Micheleburgh, MT 38471', '2018-11-25', 2, 171, 4),
('Jones Group', 1, 'Probably church body mean. Painting senior entire expect investment yard responsibility. Mrs never wrong couple site. Suddenly seek choice produce.', 4, '8644 Watson Road\nEast David, MS 53089', '2021-10-12', 3, 72, 2);
/* INSERT DATA INTO `ReferrableDoctors` TABLE */
INSERT INTO ReferrableDoctors (name, phone_number, ref_doctor_id, specialization) VALUES
('Aaron Nelson', '001-329-431-6756x2566', 1, 'Hepatobiliary'),
('Timothy Hernandez', '(327)566-7633', 2, 'Internal Medicine'),
('Dan Mckinney', '3125023949', 3, 'Neurosurgery'),
('Sean Walton', '(708)869-7747x35400', 4, 'Nephrology'),
('Gregory Roberts', '(163)968-3735', 5, 'Allergy');
/* INSERT DATA INTO `Referrals` TABLE */
INSERT INTO Referrals (emp_id, patient_id, ref_doctor_id, ref_id) VALUES
(5, 5, 3, 1),
(1, 5, 5, 2),
(3, 4, 4, 3),
(4, 5, 5, 4),
(3, 2, 1, 5);
/* INSERT DATA INTO `RelativeConditions` TABLE */
INSERT INTO RelativeConditions (icd_code, relative_id) VALUES
('A009', 1),
('A009', 2),
('A000', 2),
('A009', 3),
('A000', 3),
('A009', 4),
('A000', 5),
('A009', 5);
/* INSERT DATA INTO `Relatives` TABLE */
INSERT INTO Relatives (additional_notes, patient_id, relative_id, relative_type) VALUES
('Physical agency and difficult president at artist.', 4, 1, 'mother'),
('Itself group computer forget would section him. Through move source wonder relate service.', 2, 2, 'aunt'),
('Commercial may perform product style record. Form style star east. What to sea.', 2, 3, 'great-grandfather'),
('Until our per leader change own. Future scene heavy personal threat.', 3, 4, 'great-grandmother'),
('Public leader medical class send. Establish manage hotel financial too nearly. Significant now energy.', 4, 5, 'uncle');
/* INSERT DATA INTO `SpecializedLabs` TABLE */
INSERT INTO SpecializedLabs (address, lab_id, phone_number) VALUES
('993 Clayton Viaduct\nHunterville, NE 74689', 1, '001-183-067-5375x1007'),
('50552 Maria Fort\nChadberg, AL 27343', 2, '(116)116-2076x60754'),
('5744 White Common\nNew Beverlyburgh, FL 16915', 3, '+1-104-509-3227x17542'),
('12648 Yang Divide Suite 451\nSouth Cynthia, NC 08084', 4, '583.324.5602'),
('762 Reynolds Gateway\nPetersonhaven, MI 61113', 5, '(606)573-5471x2141');
/* INSERT DATA INTO `Tests` TABLE */
INSERT INTO Tests (test_id, test_name) VALUES
(1, 'matrix leading-edge e-business'),
(2, 'scale plug-and-play e-business'),
(3, 'whiteboard cross-platform experiences'),
(4, 'embrace distributed channels'),
(5, 'redefine integrated technologies');
/* INSERT DATA INTO `TestsAccepted` TABLE */
INSERT INTO TestsAccepted (lab_id, test_id) VALUES
(1, 2),
(1, 3),
(2, 2),
(2, 5),
(3, 3),
(3, 1),
(4, 2),
(5, 4);
