competition/scoring_program.zip:
	cd scoring_program && zip ../competition/scoring_program.zip * && cd ..

competition/dev_data.zip:
	cd dev_data && zip ../competition/dev_data.zip * && cd ..

competition/test_data.zip:
	cd test_data && zip ../competition/test_data.zip * && cd ..

competition.zip: competition/scoring_program.zip competition/dev_data.zip competition/test_data.zip
	cd competition && zip ../competition.zip * && cd ..

submission.zip:
	cd submission && zip ../submission.zip * && cd ..
