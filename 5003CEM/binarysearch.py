"""
BINARY_SEARCH(sequence, value)
	middle ← GET_MIDDLE(sequence)
	WHILE value != sequence[middle]
		IF length(sequence) > 1
			IF value > sequence[middle]
				sequence ← sequence[middle .. length(sequence)]
			ELSE
				sequence ← sequence[0 .. middle]
		ELSE
			IF value != sequence[middle]
				RETURN FALSE
		middle ← GET_MIDDLE(sequence)
	RETURN TRUE
"""
def binary_search(sequence, value):
	sequence=[0]
	def get_middle(sequence):
		while value != sequence[middle]:
			if len(sequence) > 1:
				if value > sequence[middle]:
					sequence = sequence[middle] to len(sequence)
				else:
					sequence = sequence[0] to sequence[middle]
			else:
				if value != sequence(middle):
					return False
			middle = get_middle(sequence)
		return True

sequence = [17,61,32,43,31,5,11]