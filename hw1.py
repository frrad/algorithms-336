# There are m hospitals and n residents. Each hospital has a ranking of
# each resident and each resident has a ranking of each hospital in terms
# of preference.

# Return a stable matching of hospitals to residents.

# Input will be supplied as m lists of n rankings together with n lists of
# m rankings. For example suppose there are two hospitals with the preferences
# Hospital 0: Resident 0 > Resident 1 > Resident 2
# Hospital 1: Resident 2 > Resident 1 > Resident 0
# and three residents with preferences
# Resident 0: Hospital 0 > Hospital 1
# Resident 1: Hospital 0 > Hospital 1
# Resident 2: Hospital 0 > Hospital 1
# then input would be stable_matching([[0,1,2], [2,1,0]], [[0,1],[0,1],[0,1]]).

# Return a stable matching formatted as a list of length m where the
# element in index k indicates which student is assigned to hospital k.
# In the above example, a valid answer would be [0, 2].


def stable_matching(hospital_rankings, student_rankings):
    return []
