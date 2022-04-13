/* INSERT DATA INTO `Appointment` TABLE */

INSERT INTO `Appointment` (`app_id`, `blood_pressure`, `height`, `notes`, `patient_id`, `room_number`, `temperature`, `weight`) VALUES

(1, '112/61', 55.7, None, 4, 10, 96.8, 242.26),

(2, '104/72', 71.87, None, 4, 11, 99.01, 152.92),

(3, '112/90', 71.37, None, 1, 12, 96.45, 183.5),

(4, '81/89', 63.15, 'Key beat drop step child this degree. Baby interview senior stop always Congress majority campaign. Various floor itself news experience.', 2, 2, 105.17, 233.45),

(5, '105/78', 65.42, None, 3, 17, 100.62, 326.56);

/* INSERT DATA INTO `ArchivedFile` TABLE */

INSERT INTO `ArchivedFile` (`emp_id`, `file_blob`, `file_id`, `file_name`, `patient_id`) VALUES

(1, None, 1, 'up.txt', 5),

(2, None, 2, 'make.wav', 4),

(4, None, 3, 'card.pages', 4),

(2, None, 4, 'generation.mov', 1),

(4, None, 5, 'matter.mp3', 1);

/* INSERT DATA INTO `BloodExam` TABLE */

INSERT INTO `BloodExam` (`blood_sugar`, `blood_type`, `exam_id`) VALUES

(82, 'B+', 1),

(72, 'B-', 3);

/* INSERT DATA INTO `ConductedBy` TABLE */

INSERT INTO `ConductedBy` (`lab_id`, `report_id`) VALUES

(4, 1),

(5, 2),

(4, 3),

(4, 4),

(3, 5);

/* INSERT DATA INTO `CoveredBy` TABLE */

INSERT INTO `CoveredBy` (`group_number`, `member_id`, `patient_id`, `policy_holder_name`, `provider_id`) VALUES

('843318', 'LHV886016419', 2, 'Amanda Zavala', 3),

('590262', 'RQK535749220', 2, 'Amanda Zavala', 1),

('599271', 'HYM812379332', 1, 'Thomas Moon', 1),

('778514', 'RUF089577403', 4, 'William Gonzalez', 3),

('357345', 'KXX963546030', 1, 'Thomas Moon', 3);

/* INSERT DATA INTO `CovidExam` TABLE */

INSERT INTO `CovidExam` (`exam_id`, `is_positive`, `test_type`) VALUES

(2, True, 'PCR'),

(4, False, 'PCR'),

(5, False, 'Antigen');

/* INSERT DATA INTO `Diagnosis` TABLE */

INSERT INTO `Diagnosis` (`app_id`, `comment`, `emp_id`, `icd_code`, `patient_id`) VALUES

(2, 'Pattern president add lead network the. Live teach movie I situation understand agree.', 3, 'A009', 4),

(2, 'Difficult there leg theory case north. Class on reach.', 3, 'A001', 4),

(3, 'Structure your those head. Page single theory. American focus something who blood. Certain hotel should.', 2, 'A000', 1),

(3, 'Huge away represent race sing nation network. Check clearly ahead career. Ground think save respond friend budget while.', 2, 'A009', 1),

(4, 'Recent project speech director city necessary thus sister. Tv collection still support these military part. Just raise enough onto try.', 3, 'A000', 2);

/* INSERT DATA INTO `EmpImmunization` TABLE */

INSERT INTO `EmpImmunization` (`emp_id`, `immunization_id`) VALUES

(4, 5),

(2, 4),

(5, 4),

(2, 4),

(5, 3);

/* INSERT DATA INTO `Employee` TABLE */

INSERT INTO `Employee` (`address`, `birthday`, `dea_number`, `email`, `emp_id`, `gender`, `medical_license_number`, `name`, `phone_number`, `role`, `salary`, `ssn`) VALUES

('2787 Nicole Park\nLarrymouth, MT 25142', datetime.date(1990, 6, 25), 'BT0089131', 'moralesjacqueline@example.com', 1, 'Genderfluid', 'RN-6650', 'Tonya Irwin', '093-523-3769', 'Nurse', 54965, '791-85-0767'),

('9097 Bowman Landing Apt. 369\nAlanberg, MA 44739', datetime.date(1997, 9, 22), 'MB6824173', 'darin24@example.org', 2, 'Female', 'GP-2294', 'Michelle Morgan', '+1-344-217-6104x7142', 'Physician General Practitioner', 195339, '044-06-3371'),

('96111 Kara Circle\nSmithfurt, NC 38488', datetime.date(1985, 8, 31), None, 'mendozaholly@example.com', 3, 'Female', None, 'John Richards', '281-465-4611x8775', 'Receptionist', 20482, '039-39-5490'),

('5821 Hernandez Lodge Suite 875\nBoltonborough, RI 29176', datetime.date(1970, 5, 16), None, 'nsanders@example.net', 4, 'Male', None, 'Michael Burgess', '(349)263-5110x873', 'Orderly', 17324, '044-28-2398'),

('Unit 8688 Box 0918\nDPO AP 10509', datetime.date(1965, 1, 17), 'BK0024894', 'alexis75@example.org', 5, 'Female', 'PA-7699', 'Susan Harris', '249.269.4711x80132', 'Physician Assistant', 121383, '820-20-7549');

/* INSERT DATA INTO `Exam` TABLE */

INSERT INTO `Exam` (`app_id`, `comment`, `exam_id`, `report_id`) VALUES

(4, 'Matter nice really listen meeting language condition. Fund indicate help north friend state do.', 1, 1),

(4, 'Simple improve language thousand need when simple. Involve education little direction exist.', 2, 5),

(2, None, 3, 4),

(3, None, 4, 2),

(4, None, 5, 4);

/* INSERT DATA INTO `Experiencing` TABLE */

INSERT INTO `Experiencing` (`app_id`, `comment`, `icd_code`) VALUES

(1, None, 'A009'),

(2, None, 'A009'),

(3, None, 'A000'),

(3, 'Company enter son foreign remember site military.', 'A001'),

(4, None, 'A000'),

(4, 'One political almost serious stand author possible lead.', 'A001'),

(5, None, 'A001');

/* INSERT DATA INTO `Immunization` TABLE */

INSERT INTO `Immunization` (`immunization_id`, `immunization_type`) VALUES

(1, 'Mumps'),

(2, 'Haemophilus Influenza Type B'),

(3, 'Tuberculosis'),

(4, 'Pertussis'),

(5, 'Tuberculosis');

/* INSERT DATA INTO `ImmunizedBy` TABLE */

INSERT INTO `ImmunizedBy` (`immunization_id`, `patient_id`) VALUES

(3, 4),

(2, 5),

(5, 2),

(3, 1),

(3, 3);

/* INSERT DATA INTO `InsuranceProvider` TABLE */

INSERT INTO `InsuranceProvider` (`insurance_name`, `is_in_network`, `my_policy_number`, `provider_id`) VALUES

('Snyder LLC', True, '46660', 0),

('Walls, Allen and Blair', True, '50076', 1),

('Wu-Guzman', True, '12560', 2),

('Hughes-Williams', True, '72009', 3),

('Soto Inc', True, '85367', 4);

/* INSERT DATA INTO `LabReport` TABLE */

INSERT INTO `LabReport` (`app_id`, `file_id`, `icd_code`, `info`, `report_id`, `result_info`) VALUES

(2, 5, 'A001', 'Few participant true lead. Long not improve begin.', 1, 'Father growth behind probably. Statement carry next according.'),

(3, 3, 'A009', 'Make real use nice themselves gas best above. Marriage worker ever across great.', 2, 'Back off difficult happen. Team certainly explain current simply process. Executive partner story budget great than.'),

(3, 4, 'A009', 'Trouble it grow husband short year term look. Building child usually sea upon.', 3, 'Body himself home message woman. Stock determine human find discussion military ability. First through dinner whose worker offer American.'),

(3, 3, 'A000', 'Rise condition Congress recognize agreement.', 4, 'Movement can start paper tree bank.'),

(1, 1, 'A001', 'Minute perform indeed.', 5, 'Dinner indeed listen a decision. Past especially old.');

/* INSERT DATA INTO `MedicalStaff` TABLE */

INSERT INTO `MedicalStaff` (`app_id`, `emp_id`) VALUES

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

/* INSERT DATA INTO `Patient` TABLE */

INSERT INTO `Patient` (`address`, `birthday`, `email`, `gender`, `name`, `patient_id`, `phone_number`, `ssn`) VALUES

('578 Michael Island\nNew Thomas, NC 34644', datetime.date(1971, 10, 16), 'montgomeryjohn@example.net', 'Male', 'Thomas Moon', 1, '(604)876-4759x3824', '723-78-2408'),

('583 Wallace Ranch\nStewartbury, HI 25324', datetime.date(1968, 6, 27), 'kaisernancy@example.com', 'Male', 'Amanda Zavala', 2, '(097)535-1393x3287', '112-39-9032'),

('515 Tom Roads Suite 330\nDavebury, WY 22846', datetime.date(2017, 7, 6), 'melissajacobson@example.net', 'Male', 'Robert Garcia', 3, '122-018-6848', '846-54-9498'),

('00869 Mary Cliff Apt. 145\nWhitehaven, AZ 78683', datetime.date(1968, 7, 5), 'martha10@example.net', 'Male', 'William Gonzalez', 4, '001-309-891-0139x916', '023-25-3031'),

('80715 Amy Dale Apt. 759\nEmilyshire, SC 81906', datetime.date(1963, 3, 7), 'kmaldonado@example.net', 'Genderfluid', 'Eric Goodman', 5, '001-792-302-2584x1972', '319-84-5852');

/* INSERT DATA INTO `Pharmacy` TABLE */

INSERT INTO `Pharmacy` (`pharmacy_address`, `pharmacy_name`) VALUES

('3407 Smith Hills\nPort Tiffanyport, PA 20977', 'Mccarthy-Ruiz'),

('640 Joseph Skyway\nNorth Jonathanhaven, OR 93557', 'Wallace-Francis'),

('101 Torres Junctions\nNew Micheleburgh, MT 38471', 'Meyer-Berry'),

('8644 Watson Road\nEast David, MS 53089', 'Mcdonald, Castro and Evans'),

('77857 Scott Divide Suite 093\nWest Thomastown, NC 09211', 'Camacho, Parks and Harmon');

/* INSERT DATA INTO `Prescription` TABLE */

INSERT INTO `Prescription` (`drug_name`, `emp_id`, `instructions`, `patient_id`, `pharmacy_address`, `prescription_date`, `prescription_id`, `quantity`, `refills`) VALUES

('Park, Hickman and Cooley', 3, 'Break word source wall drug. Race government trouble tonight former section across. North weight guy. Fall manager idea issue color small notice kind.', 4, '8644 Watson Road\nEast David, MS 53089', datetime.date(2018, 3, 8), 1, 54, 5),

('Fry Group', 3, None, 1, '101 Torres Junctions\nNew Micheleburgh, MT 38471', datetime.date(2020, 6, 27), 2, 171, 4),

('Jones Group', 1, 'Probably church body mean. Painting senior entire expect investment yard responsibility. Mrs never wrong couple site. Suddenly seek choice produce.', 4, '8644 Watson Road\nEast David, MS 53089', datetime.date(2021, 12, 5), 3, 72, 2);

/* INSERT DATA INTO `ReferrableDoctor` TABLE */

INSERT INTO `ReferrableDoctor` (`name`, `phone_number`, `ref_doctor_id`, `specialization`) VALUES

('Aaron Nelson', '001-329-431-6756x2566', 1, 'Hepatobiliary'),

('Timothy Hernandez', '(327)566-7633', 2, 'Internal Medicine'),

('Dan Mckinney', '3125023949', 3, 'Neurosurgery'),

('Sean Walton', '(708)869-7747x35400', 4, 'Nephrology'),

('Gregory Roberts', '(163)968-3735', 5, 'Allergy');

/* INSERT DATA INTO `Referral` TABLE */

INSERT INTO `Referral` (`emp_id`, `patient_id`, `ref_doctor_id`, `ref_id`) VALUES

(5, 5, 3, 1),

(1, 5, 5, 2),

(3, 4, 4, 3),

(4, 5, 5, 4),

(3, 2, 1, 5);

/* INSERT DATA INTO `RelativeCondition` TABLE */

INSERT INTO `RelativeCondition` (`icd_code`, `relative_id`) VALUES

('A009', 1),

('A009', 2),

('A000', 2),

('A009', 3),

('A000', 3),

('A009', 4),

('A000', 5),

('A009', 5);

/* INSERT DATA INTO `Relative` TABLE */

INSERT INTO `Relative` (`additional_notes`, `patient_id`, `relative_id`, `relative_type`) VALUES

('Physical agency and difficult president at artist.', 4, 1, 'mother'),

('Itself group computer forget would section him. Through move source wonder relate service.', 2, 2, 'aunt'),

('Commercial may perform product style record. Form style star east. What to sea.', 2, 3, 'great-grandfather'),

('Until our per leader change own. Future scene heavy personal threat.', 3, 4, 'great-grandmother'),

('Public leader medical class send. Establish manage hotel financial too nearly. Significant now energy.', 4, 5, 'uncle');

/* INSERT DATA INTO `SpecializedLab` TABLE */

INSERT INTO `SpecializedLab` (`address`, `lab_id`, `phone_number`) VALUES

('993 Clayton Viaduct\nHunterville, NE 74689', 1, '001-183-067-5375x1007'),

('50552 Maria Fort\nChadberg, AL 27343', 2, '(116)116-2076x60754'),

('5744 White Common\nNew Beverlyburgh, FL 16915', 3, '+1-104-509-3227x17542'),

('12648 Yang Divide Suite 451\nSouth Cynthia, NC 08084', 4, '583.324.5602'),

('762 Reynolds Gateway\nPetersonhaven, MI 61113', 5, '(606)573-5471x2141');

/* INSERT DATA INTO `Test` TABLE */

INSERT INTO `Test` (`test_id`, `test_name`) VALUES

(1, 'matrix leading-edge e-business'),

(2, 'scale plug-and-play e-business'),

(3, 'whiteboard cross-platform experiences'),

(4, 'embrace distributed channels'),

(5, 'redefine integrated technologies');

/* INSERT DATA INTO `TestAccepted` TABLE */

INSERT INTO `TestAccepted` (`lab_id`, `test_id`) VALUES

(1, 2),

(1, 3),

(2, 2),

(2, 5),

(3, 3),

(3, 1),

(4, 2),

(5, 4);

