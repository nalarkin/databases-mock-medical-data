/* INSERT DATA INTO `accepted_tests` TABLE */
INSERT INTO accepted_tests (lab_id, test_id) VALUES
(1, 1),
(2, 3),
(2, 2),
(3, 1),
(3, 3),
(4, 1),
(5, 3);
/* INSERT DATA INTO `administered_vaccines` TABLE */
INSERT INTO administered_vaccines (exam_id, vaccine_type) VALUES
(1, 'Hepatitis B'),
(3, 'Tuberculosis');
/* INSERT DATA INTO `appointment_employees` TABLE */
INSERT INTO appointment_employees (app_id, emp_id) VALUES
(1, 3),
(1, 4),
(1, 1),
(2, 2),
(2, 3),
(2, 1),
(3, 1),
(3, 4),
(4, 5),
(4, 3),
(5, 3),
(5, 4),
(5, 2);
/* INSERT DATA INTO `appointment_medical_conditions` TABLE */
INSERT INTO appointment_medical_conditions (app_id, comment, icd_code) VALUES
(1, DEFAULT, 'A000'),
(2, DEFAULT, 'A001'),
(3, 'So teach energy possible believe step. Grow better why child might source.', 'A001'),
(3, 'Front war receive civil single city.', 'A000'),
(4, DEFAULT, 'A009'),
(5, DEFAULT, 'A001');
/* INSERT DATA INTO `appointments` TABLE */
INSERT INTO appointments (app_id, blood_pressure, date, height, notes, patient_id, room_number, temperature, weight) VALUES
(1, '112/61', TIMESTAMP '2021-05-30 09:29:58', 55.7, DEFAULT, 4, 10, 96.8, 242.26),
(2, '105/76', TIMESTAMP '2021-08-11 16:31:24', 72.07, 'Gas Republican and various authority leave right. True include management.', 4, 6, 99.12, 291.98),
(3, '90/65', TIMESTAMP '2020-09-16 16:58:33', 74.79, 'Baby interview senior stop always Congress majority campaign. Various floor itself news experience. Smile represent since method left plant evening.', 1, 3, 97.54, 149.58),
(4, '158/66', TIMESTAMP '2022-01-29 04:31:38', 62.44, DEFAULT, 2, 3, 98.18, 126.95),
(5, '148/92', TIMESTAMP '2021-09-30 23:23:06', 51.49, 'Grow push region produce develop story drive. Film force health lose old case administration.', 3, 0, 99.85, 211.33);
/* INSERT DATA INTO `archived_files` TABLE */
INSERT INTO archived_files (emp_id, file_blob, file_id, file_name, patient_id) VALUES
(2, DEFAULT, 1, 'free.flac', 5),
(3, DEFAULT, 2, 'similar.flac', 2),
(5, DEFAULT, 3, 'green.bmp', 5),
(3, DEFAULT, 4, 'another.avi', 1),
(5, DEFAULT, 5, 'assume.txt', 3);
/* INSERT DATA INTO `blood_exams` TABLE */
INSERT INTO blood_exams (blood_sugar, blood_type, exam_id) VALUES
(94, 'O-', 4),
(75, 'O+', 5);
/* INSERT DATA INTO `covid_exams` TABLE */
INSERT INTO covid_exams (exam_id, is_positive, test_type) VALUES
(2, False, 'Antigen');
/* INSERT DATA INTO `diagnoses` TABLE */
INSERT INTO diagnoses (app_id, comment, emp_id, icd_code, patient_id) VALUES
(1, 'Early high trouble drive loss turn. Structure your those head. Page single theory.', 4, 'A001', 4),
(2, 'Fast play fact issue radio especially. Get car party close issue. Less politics religious back international risk. College debate direction moment.', 1, 'A009', 4),
(3, 'Once effect main simply two no. Sister meet though ago. These military part decade.', 3, 'A009', 1),
(4, 'Growth behind probably arm. Only cup almost identify.', 4, 'A001', 2),
(4, 'Grow husband short year term. Tough building child usually sea upon full. Body himself home message woman.', 4, 'A000', 2),
(5, 'Job high she. West agreement girl happen front law care military. War resource evening realize per.', 5, 'A000', 3),
(5, 'Feel military pull watch choice. Free perform civil.', 5, 'A001', 3);
/* INSERT DATA INTO `employees` TABLE */
INSERT INTO employees (address, birthday, dea_number, email, emp_id, gender, medical_license_number, name, phone_number, role, salary, ssn) VALUES
('027 Jonathon Estate Suite 878\nNorth Troyport, NH 07035', '2012-04-13', 'MG0300891', 'rgray@example.net', 1, 'Male', 'GP2066', 'Sheri Burnett', '(466)109-3523', 'Physician General Practitioner', 255099, '896-54-0517'),
('24000 Erin Point Suite 590\nJosephmouth, NE 49318', '2013-02-27', 'BS5900422', 'hmarsh@example.com', 2, 'Male', 'RN4555', 'Cassandra Bennett', '934-421-7610', 'Nurse', 63897, '137-84-8534'),
('71760 Rogers Spur Apt. 296\nNorth Lindseyborough, IN 08516', '2015-05-07', DEFAULT, 'kevin11@example.net', 3, 'Male', DEFAULT, 'Brent Hawkins', '568-241-7304x2814', 'Receptionist', 66661, '493-61-5523'),
('76430 Cindy Cove\nSouth Nicholas, FL 14230', '2014-08-02', 'BI0555082', 'brownmichelle@example.net', 4, 'Female', 'PA5773', 'Victoria Hernandez MD', '001-361-534-9263', 'Physician Assistant', 126466, '029-68-7400'),
('Unit 8688 Box 0918\nDPO AP 10509', '2013-08-06', 'BK0024894', 'blakeshane@example.org', 5, 'Female', 'PA7699', 'Susan Harris', '+1-269-471-1801x320', 'Physician Assistant', 121383, '820-20-7549');
/* INSERT DATA INTO `exams` TABLE */
INSERT INTO exams (app_id, comment, exam_id, report_id) VALUES
(2, DEFAULT, 1, 3),
(3, 'First natural without any remain support.', 2, 1),
(4, DEFAULT, 3, 5),
(1, DEFAULT, 4, 5),
(5, 'Argue home exactly different week treat mouth threat.', 5, 1);
/* INSERT DATA INTO `immunizations` TABLE */
INSERT INTO immunizations (immunization_id, immunization_type) VALUES
(1, 'Mumps'),
(2, 'Haemophilus Influenza Type B'),
(3, 'Tuberculosis'),
(4, 'Pertussis'),
(5, 'Tuberculosis');
/* INSERT DATA INTO `immunized_employees` TABLE */
INSERT INTO immunized_employees (emp_id, immunization_id) VALUES
(1, 4),
(5, 2),
(3, 2),
(1, 5),
(3, 5);
/* INSERT DATA INTO `immunized_patients` TABLE */
INSERT INTO immunized_patients (immunization_id, patient_id) VALUES
(4, 1),
(4, 3),
(5, 5),
(2, 2),
(3, 2);
/* INSERT DATA INTO `insurance_covers` TABLE */
INSERT INTO insurance_covers (group_number, member_id, patient_id, policy_holder_name, provider_id) VALUES
('957740', 'TAQ236599271', 2, 'Randall Costa II', 5),
('354603', 'TMW827785142', 3, 'Savannah Robinson', 3),
('802507', 'ALS535734524', 1, 'Thomas Moon', 1),
('237625', 'LVN003003510', 1, 'Thomas Moon', 4),
('709166', 'ZXV256606488', 2, 'Amanda Zavala', 4);
/* INSERT DATA INTO `insurance_providers` TABLE */
INSERT INTO insurance_providers (insurance_name, is_in_network, policy_number, provider_id) VALUES
('Snyder LLC', True, '46660', 1),
('Walls, Allen and Blair', True, '50076', 2),
('Wu-Guzman', True, '12560', 3),
('Hughes-Williams', True, '72009', 4),
('Soto Inc', True, '85367', 5);
/* INSERT DATA INTO `lab_reports` TABLE */
INSERT INTO lab_reports (app_id, file_id, icd_code, info, report_id, result_info) VALUES
(1, 5, 'A009', 'Charge read management production up our. Drug toward such.', 1, 'Analysis care kitchen. Difference range technology serious international position write those.'),
(5, 1, 'A001', 'Clear newspaper ground just keep. Suffer life chair senior seem west.', 2, 'Decide happy another image because include now. Must plant whether protect most trade. Herself Mr bad wide manage.'),
(4, 2, 'A000', 'Pay growth base age speak pass.', 3, 'Happen letter body language there wonder him. Until direction opportunity very analysis firm once. As year look floor role agency its. Seven those budget involve.'),
(2, 3, 'A001', 'Enough break factor pattern PM. My full need claim many against television.', 4, 'Yet between night western serious edge. Minute technology only magazine.'),
(4, 3, 'A000', 'Best student describe concern professional discover.', 5, 'Give especially win give yourself system. Letter finish campaign night simply. Bar standard final. Along particularly factor boy Republican without.');
/* INSERT DATA INTO `patients` TABLE */
INSERT INTO patients (address, birthday, email, gender, name, patient_id, phone_number, ssn) VALUES
('578 Michael Island\nNew Thomas, NC 34644', '2010-11-12', 'montgomeryjohn@example.net', 'Male', 'Thomas Moon', 1, '(604)876-4759x3824', '723-78-2408'),
('583 Wallace Ranch\nStewartbury, HI 25324', '2010-01-14', 'kaisernancy@example.com', 'Male', 'Amanda Zavala', 2, '(097)535-1393x3287', '112-39-9032'),
('59179 Bruce Gardens Apt. 413\nLauramouth, AR 13687', '2012-06-29', 'pattylawrence@example.com', 'Genderfluid', 'Savannah Robinson', 3, '122-018-6848', '594-36-7383'),
('086 Mary Cliff\nNorth Deborah, NE 24135', '2018-10-15', 'leetara@example.net', 'Female', 'John Carlson', 4, '+1-891-013-9916x1510', '127-62-3451'),
('564 Ann Bridge Suite 150\nDennisfort, RI 38233', '2018-08-22', 'awade@example.com', 'Genderfluid', 'Leslie Mcclain', 5, '(345)792-3022x5841', '698-53-9325');
/* INSERT DATA INTO `pharmacies` TABLE */
INSERT INTO pharmacies (pharmacy_address, pharmacy_name) VALUES
('3407 Smith Hills\nPort Tiffanyport, PA 20977', 'Mccarthy-Ruiz'),
('640 Joseph Skyway\nNorth Jonathanhaven, OR 93557', 'Wallace-Francis'),
('101 Torres Junctions\nNew Micheleburgh, MT 38471', 'Meyer-Berry'),
('8644 Watson Road\nEast David, MS 53089', 'Mcdonald, Castro and Evans'),
('77857 Scott Divide Suite 093\nWest Thomastown, NC 09211', 'Camacho, Parks and Harmon');
/* INSERT DATA INTO `prescriptions` TABLE */
INSERT INTO prescriptions (drug_name, emp_id, instructions, patient_id, pharmacy_address, prescription_date, prescription_id, quantity, refills) VALUES
('Kramer PLC', 2, 'We lose water. Section could nature interest wear. Morning as police often. Place myself his itself find add sing. Watch Mrs never wrong couple.', 4, '77857 Scott Divide Suite 093\nWest Thomastown, NC 09211', TIMESTAMP '2021-10-19 16:38:56', 1, 12, 7),
('Moody-Kirk', 4, 'Guess we no in pass sound. Tonight gun word citizen create. Physical market room eat through ever. Back large season last meeting southern. When clearly type up. Wait education think similar particular before.', 4, '101 Torres Junctions\nNew Micheleburgh, MT 38471', TIMESTAMP '2008-12-31 02:15:53', 2, 131, 2),
('Smith-King', 2, 'Recent state old great notice north. Foreign agency list miss among. Ten guess attorney response provide likely fire. Fire town worker. Image central challenge term memory. By care lose politics. Role mind statement.', 5, '77857 Scott Divide Suite 093\nWest Thomastown, NC 09211', TIMESTAMP '2020-03-30 17:48:27', 3, 102, 6);
/* INSERT DATA INTO `referrable_doctors` TABLE */
INSERT INTO referrable_doctors (name, phone_number, ref_doctor_id, specialization) VALUES
('Aaron Nelson', '001-329-431-6756x2566', 1, 'Hepatobiliary'),
('Timothy Hernandez', '(327)566-7633', 2, 'Internal Medicine'),
('Dan Mckinney', '3125023949', 3, 'Neurosurgery'),
('Sean Walton', '(708)869-7747x35400', 4, 'Nephrology'),
('Gregory Roberts', '(163)968-3735', 5, 'Allergy');
/* INSERT DATA INTO `referrals` TABLE */
INSERT INTO referrals (emp_id, patient_id, ref_doctor_id, ref_id) VALUES
(4, 2, 4, 1),
(1, 4, 3, 2),
(4, 3, 2, 3),
(5, 3, 3, 4),
(1, 3, 1, 5);
/* INSERT DATA INTO `relative_conditions` TABLE */
INSERT INTO relative_conditions (icd_code, relative_id) VALUES
('A000', 1),
('A009', 1),
('A009', 2),
('A001', 3),
('A000', 3),
('A001', 4),
('A000', 5);
/* INSERT DATA INTO `relatives` TABLE */
INSERT INTO relatives (additional_notes, patient_id, relative_id, relative_type) VALUES
('Style star east against southern. Sea stuff no response. Until our per leader change own.', 1, 1, 'mother'),
('Personal threat many. Fall character door green save identify. Sound war address morning explain.', 3, 2, 'grandmother'),
('Need various although house build get anything. Science alone quite old simply. Yet seven several might history.', 4, 3, 'uncle'),
('Word source wall drug purpose mouth then. Trouble tonight former section.', 4, 4, 'grandmother'),
(DEFAULT, 5, 5, 'sister');
/* INSERT DATA INTO `report_creators` TABLE */
INSERT INTO report_creators (lab_id, report_id) VALUES
(3, 1),
(2, 2),
(3, 3),
(3, 4),
(3, 5);
/* INSERT DATA INTO `specialized_labs` TABLE */
INSERT INTO specialized_labs (address, lab_id, phone_number) VALUES
('993 Clayton Viaduct\nHunterville, NE 74689', 1, '001-183-067-5375x1007'),
('50552 Maria Fort\nChadberg, AL 27343', 2, '(116)116-2076x60754'),
('5744 White Common\nNew Beverlyburgh, FL 16915', 3, '+1-104-509-3227x17542'),
('12648 Yang Divide Suite 451\nSouth Cynthia, NC 08084', 4, '583.324.5602'),
('762 Reynolds Gateway\nPetersonhaven, MI 61113', 5, '(606)573-5471x2141');
/* INSERT DATA INTO `tests` TABLE */
INSERT INTO tests (test_id, test_name) VALUES
(1, 'matrix leading-edge e-business'),
(2, 'scale plug-and-play e-business'),
(3, 'whiteboard cross-platform experiences'),
(4, 'embrace distributed channels'),
(5, 'redefine integrated technologies');
