def writeAlyaSld(file, filename, dash_iload, kfl_timei, kfl_coh, nmate, iload, debug):
    """ Alya caseName.sld.dat file
    """
    
    stream = open(file, 'w')

    stream.write('$-------------------------------------------------------------------\n')
    stream.write('$\n')
    stream.write(f'$ {filename+dash_iload:s}\n')
    stream.write('$\n')
    stream.write('$ Details:\n')
    stream.write('$\n')
    stream.write('$  Materials:\n')
    stream.write('$  CODE 1: MATRIX\n')
    stream.write('$  CODE 2: FIBER\n')
    stream.write('$  CODE 3: DAMAGED FIBER (OPTIONAL)\n')
    stream.write('$   ...\n')
    stream.write('$  CODE N: COHESIVE (OPTIONAL)\n')
    stream.write('$\n')
    stream.write('$  Boundary codes:\n')
    stream.write('$  CODE 1: LEFT,  X= 0\n')
    stream.write('$  CODE 2: RIGHT, X= 1\n')
    stream.write('$  CODE 3: BOT,   Y= 0\n')
    stream.write('$  CODE 4: TOP,   Y= 1\n')
    stream.write('$  CODE 5: BACK,  Z= 0\n')
    stream.write('$  CODE 6: FRONT, Z= 1\n')
    stream.write('$\n')
    stream.write('$ Units:     SI (-)\n')
    stream.write('$\n')
    stream.write('$ Reference:\n')
    stream.write('$\n')
    stream.write('$-------------------------------------------------------------------\n')
    stream.write('PHYSICAL_PROBLEM\n')
    stream.write('  PROBLEM_DEFINITION\n')
    if kfl_timei == 'STATIC':
        stream.write('    TEMPORAL_DERIVATIVES: STATIC\n')
    else:
        stream.write('    TEMPORAL_DERIVATIVES: DYNAMIC\n')
    stream.write('    NLGEOM:               OFF\n')
    stream.write('    THERMAL_ANALYSIS:     OFF\n')
    stream.write('  END_PROBLEM_DEFINITION\n')
    stream.write('  PROPERTIES\n')
    stream.write('    MATERIAL          = 1\n')
    stream.write(f'    DENSITY           = {7.8e-9:1.4e}\n' )
    stream.write('    CONSTITUTIVE_MODEL: ISOTROPIC \ \n')
    stream.write(f'      {4.20426e+03:1.4e} {0.343217:1.4f}\n')
    stream.write('    MATERIAL          = 2\n')
    stream.write(f'    DENSITY           = {7.8e-9:1.4e}\n' )
    stream.write('    CONSTITUTIVE_MODEL: ORTHOTROPIC \ \n')
    stream.write(f'      {2.17984e+05:1.4e} {1.53718e+04:1.4e} {1.4909e+04:1.4e} {0.207014:1.4f} {0.193843:1.4f} {0.0744462:1.4f} {1.39533e+04:1.4e} {1.5529e+04:1.4e} {6.80097e+03:1.4e}\n')
    nmate_aux = nmate
    if kfl_coh == True:
        nmate_aux = nmate_aux - 1
    for imate in range(nmate_aux-2):
        stream.write(f'    MATERIAL          = {imate+3}\n')
        stream.write(f'    DENSITY           = {7.8e-9:1.4e}\n' )
        stream.write('    CONSTITUTIVE_MODEL: ORTHOTROPIC \ \n')
        stream.write(f'      {2.30969e+05:1.4e} {1.63346e+04:1.4e} {1.48991e+04:1.4e} {0.20597:1.4f} {0.210491:1.4f} {0.0705096:1.4f} {1.5481e+04:1.4e} {1.47437e+04:1.4e} {6.48991e+03:1.4e}\n')
    if kfl_coh == True:
        stream.write(f'    MATERIAL          = {nmate}\n')
        stream.write(f'    DENSITY           = {7.8e-9:1.4e} {1e+6:1.1e}\n')
        stream.write('    COHESIVE_MODEL: TURON, CURRENT \ \n')
        stream.write(f'      {0.308:1.4f} {0.828:1.4f} {19.0:1.4f} {31.2:1.4f} {1.75:1.4f} {1e6:1.1e} {0.0:1.4f} {0.0:1.4f} {0.001:1.4f}\n')
    stream.write('  END_PROPERTIES\n')
    stream.write('  PARAMETERS\n')
    stream.write('    CSYS_MATERIAL: FIELD= 1, VECTORS\n')
    stream.write('  END_PARAMETERS\n')
    stream.write('END_PHYSICAL_PROBLEM\n')
    stream.write('$-------------------------------------------------------------------\n')
    stream.write('NUMERICAL_TREATMENT\n')
    stream.write('  TIME_TREATMENT:       IMPLICIT\n')
    stream.write('  TIME_INTEGRATION:     NEWMARK, DAMPED\n')
    stream.write('  STEADY_STATE:         OFF\n')
    stream.write('  ALGEBRAIC_SOLVER\n')
    stream.write('    SOLVER:             CG\n')
    stream.write('$    SOLVER:             GMRES, KRYLOV= 200\n')
    stream.write('    CONVERGENCE:        ITERATIONS= 500, TOLERANCE= 1.0E-6\n')
    stream.write('    PRECONDITIONER:     DIAGONAL\n')
    stream.write('    COARSE:             OFF\n')
    stream.write('    OPTIONS:            ZERO_FIXITY\n')
    if debug:
        stream.write('    OUTPUT:             CONVERGENCE\n')
    stream.write('  END_ALGEBRAIC_SOLVER\n')
    stream.write('  RESIDUAL:             ALL\n') 
    stream.write('  SAFETY_FACTOR=        1.0\n') 
    stream.write('  CONVERGENCE_TOLER=    1.0E-3\n')
    stream.write('  MAXIMUM_ITERATION=    200\n')  
    stream.write('  VECTORIZED_ASSEMBLY:  OFF\n')
    stream.write('END_NUMERICAL_TREATMENT\n')
    stream.write('$-------------------------------------------------------------------\n')
    stream.write('OUTPUT_&_POST_PROCESS\n')
    if debug:
        stream.write('  START_POSTPROCESS_AT: STEP= 0\n')
        stream.write('  POSTPROCESS PARTI\n')
        stream.write('  POSTPROCESS PMATE\n')
        stream.write('  POSTPROCESS FIXNO\n')
        stream.write('  POSTPROCESS BOCOD\n')
        stream.write('  POSTPROCESS PERIO\n')
        stream.write('  POSTPROCESS NPOIN\n')
        stream.write('  POSTPROCESS NELEM\n')
        stream.write('  POSTPROCESS BOSET\n')
        stream.write('  POSTPROCESS ELSET\n')
        stream.write('$  POSTPROCESS NOSET\n')
        stream.write('  POSTPROCESS AXIS1\n')
        stream.write('  POSTPROCESS AXIS2\n')
        stream.write('  POSTPROCESS AXIS3\n')
        stream.write('  POSTPROCESS ELNOR\n')
        stream.write('  POSTPROCESS STACK\n')
        stream.write('  POSTPROCESS PELCH\n')
        stream.write('  POSTPROCESS PELTY\n')
        stream.write('  POSTPROCESS SRPRO\n')
        stream.write('  POSTPROCESS BVESS\n')
        stream.write('  POSTPROCESS DISPL\n')
        stream.write('  POSTPROCESS DAMAG\n')
        stream.write('  POSTPROCESS DCOHE\n')
    stream.write('  ELEMENT_SET\n')
    if iload == '11':
        # Longitudinal tension
        stream.write('    EPSZZ\n')
        stream.write('    SIGZZ\n')
    elif iload == '22':
        # Transverse tension
        stream.write('    EPSYY\n')
        stream.write('    SIGYY\n')
    elif iload == '12':
        # In-plane shear
        stream.write('    EPSXZ\n')
        stream.write('    SIGXZ\n')
    elif iload == '23':
        # Transverse shear
        stream.write('    EPSYZ\n')
        stream.write('    SIGYZ\n')
    stream.write('  END_ELEMENT_SET\n')
    stream.write('END_OUTPUT_&_POST_PROCESS\n')
    stream.write('$-------------------------------------------------------------------\n')
    stream.write('BOUNDARY_CONDITIONS, TRANSIENT\n')
    stream.write('  CODES, NODES\n')
    if iload == '11':
        # Longitudinal tension
        stream.write('            5 001 0.0 0.0 0.0 \n')
        stream.write('        1 & 5 001 0.0 0.0 0.0 \n')
        stream.write('        2 & 5 001 0.0 0.0 0.0 \n')
        stream.write('        3 & 5 001 0.0 0.0 0.0 \n')
        stream.write('        4 & 5 001 0.0 0.0 0.0 \n')
        stream.write('    1 & 3 & 5 001 0.0 0.0 0.0 \n')
        stream.write('    1 & 4 & 5 001 0.0 0.0 0.0 \n')
        stream.write('    2 & 3 & 5 001 0.0 0.0 0.0 \n')
        stream.write('    2 & 4 & 5 001 0.0 0.0 0.0 \n')
        stream.write('            6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        1 & 6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        2 & 6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        3 & 6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        4 & 6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    1 & 3 & 6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    2 & 3 & 6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    2 & 4 & 6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    1 & 4 & 6 001 0.0 0.0 1.0, DISCRETE_FUNCTIONS= U_FUNC \n')
    elif iload == '22':
        # Transverse tension
        stream.write('            3 010 0.0 0.0 0.0 \n')
        stream.write('        1 & 3 010 0.0 0.0 0.0 \n')
        stream.write('        2 & 3 010 0.0 0.0 0.0 \n')
        stream.write('        5 & 3 010 0.0 0.0 0.0 \n')
        stream.write('        6 & 3 010 0.0 0.0 0.0 \n')
        stream.write('    1 & 5 & 3 010 0.0 0.0 0.0 \n')
        stream.write('    1 & 6 & 3 010 0.0 0.0 0.0 \n')
        stream.write('    2 & 5 & 3 010 0.0 0.0 0.0 \n')
        stream.write('    2 & 6 & 3 010 0.0 0.0 0.0 \n')
        stream.write('            4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        1 & 4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        2 & 4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        5 & 4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        6 & 4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    1 & 5 & 4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    1 & 6 & 4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    2 & 5 & 4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    2 & 6 & 4 010 0.0 1.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
    elif iload == '12':
        # In-plane shear
        stream.write('            5 100 0.0 0.0 0.0 \n')
        stream.write('        1 & 5 100 0.0 0.0 0.0 \n')
        stream.write('        2 & 5 100 0.0 0.0 0.0 \n')
        stream.write('        3 & 5 100 0.0 0.0 0.0 \n')
        stream.write('        4 & 5 100 0.0 0.0 0.0 \n')
        stream.write('    1 & 3 & 5 100 0.0 0.0 0.0 \n')
        stream.write('    1 & 4 & 5 100 0.0 0.0 0.0 \n')
        stream.write('    2 & 3 & 5 100 0.0 0.0 0.0 \n')
        stream.write('    2 & 4 & 5 100 0.0 0.0 0.0 \n')
        stream.write('            6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        1 & 6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        2 & 6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        3 & 6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        4 & 6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    1 & 3 & 6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    2 & 3 & 6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    2 & 4 & 6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    1 & 4 & 6 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
    elif iload == '23':
        # Transverse shear
        stream.write('            3 100 0.0 0.0 0.0 \n')
        stream.write('        1 & 3 100 0.0 0.0 0.0 \n')
        stream.write('        2 & 3 100 0.0 0.0 0.0 \n')
        stream.write('        5 & 3 100 0.0 0.0 0.0 \n')
        stream.write('        6 & 3 100 0.0 0.0 0.0 \n')
        stream.write('    1 & 5 & 3 100 0.0 0.0 0.0 \n')
        stream.write('    1 & 6 & 3 100 0.0 0.0 0.0 \n')
        stream.write('    2 & 5 & 3 100 0.0 0.0 0.0 \n')
        stream.write('    2 & 6 & 3 100 0.0 0.0 0.0 \n')
        stream.write('            4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        1 & 4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        2 & 4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        5 & 4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('        6 & 4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    1 & 5 & 4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    1 & 6 & 4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    2 & 5 & 4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
        stream.write('    2 & 6 & 4 100 1.0 0.0 0.0, DISCRETE_FUNCTIONS= U_FUNC \n')
    stream.write('  END_CODES\n')
    stream.write('END_BOUNDARY_CONDITIONS\n')
    stream.write('$-------------------------------------------------------------------\n')
    
    stream.close()

    
