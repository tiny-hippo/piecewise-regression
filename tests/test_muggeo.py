import copy

import pandas as pd
import numpy as np
import unittest

import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from piecewise_regression.main import Muggeo, Fit


class TestMuggeo(unittest.TestCase):

    def test_against_muggeo_r_package_data_1(self):
        """
        Muggeo uses slightly different packages and methods etc, so just check values are very close, not exact
        Starting from Muggeo's converged breakpoint values, I am iterating once, slight change
        The NextBreakpoint class is very vanilla, so in this example is getting in some local minima
        """

        xx = np.array([0.0, 0.10050251256281408, 0.20100502512562815, 0.30150753768844224, 0.4020100502512563, 0.5025125628140704, 0.6030150753768845, 0.7035175879396985, 0.8040201005025126, 0.9045226130653267, 1.0050251256281408, 1.105527638190955, 1.206030150753769, 1.306532663316583, 1.407035175879397, 1.5075376884422111, 1.6080402010050252, 1.7085427135678393, 1.8090452261306533, 1.9095477386934674, 2.0100502512562817, 2.1105527638190957, 2.21105527638191, 2.311557788944724, 2.412060301507538, 2.512562814070352, 2.613065326633166, 2.71356783919598, 2.814070351758794, 2.9145728643216082, 3.0150753768844223, 3.1155778894472363, 3.2160804020100504, 3.3165829145728645, 3.4170854271356785, 3.5175879396984926, 3.6180904522613067, 3.7185929648241207, 3.819095477386935, 3.919597989949749, 4.020100502512563, 4.120603015075377, 4.2211055276381915, 4.3216080402010055, 4.42211055276382, 4.522613065326634, 4.623115577889448, 4.723618090452262, 4.824120603015076, 4.92462311557789, 5.025125628140704, 5.125628140703518, 5.226130653266332, 5.326633165829146, 5.42713567839196, 5.527638190954774, 5.628140703517588, 5.728643216080402, 5.8291457286432165, 5.9296482412060305, 6.030150753768845, 6.130653266331659, 6.231155778894473, 6.331658291457287, 6.432160804020101, 6.532663316582915, 6.633165829145729, 6.733668341708543, 6.834170854271357, 6.934673366834171, 7.035175879396985, 7.135678391959799, 7.236180904522613, 7.336683417085427, 7.437185929648241, 7.5376884422110555, 7.63819095477387, 7.738693467336684, 7.839195979899498, 7.939698492462312, 8.040201005025127, 8.14070351758794, 8.241206030150755, 8.341708542713569, 8.442211055276383, 8.542713567839197, 8.643216080402011, 8.743718592964825, 8.84422110552764, 8.944723618090453, 9.045226130653267, 9.145728643216081, 9.246231155778895, 9.34673366834171, 9.447236180904524, 9.547738693467338, 9.648241206030152, 9.748743718592966, 9.84924623115578, 9.949748743718594, 10.050251256281408, 10.150753768844222, 10.251256281407036, 10.35175879396985, 10.452261306532664, 10.552763819095478, 10.653266331658292, 10.753768844221106, 10.85427135678392, 10.954773869346734, 11.055276381909549, 11.155778894472363, 11.256281407035177, 11.35678391959799, 11.457286432160805, 11.557788944723619, 11.658291457286433, 11.758793969849247, 11.859296482412061, 11.959798994974875, 12.06030150753769, 12.160804020100503, 12.261306532663317, 12.361809045226131, 12.462311557788945, 12.56281407035176, 12.663316582914574, 12.763819095477388, 12.864321608040202, 12.964824120603016, 13.06532663316583, 13.165829145728644, 13.266331658291458, 13.366834170854272, 13.467336683417086, 13.5678391959799, 13.668341708542714, 13.768844221105528, 13.869346733668342, 13.969849246231156, 14.07035175879397, 14.170854271356784, 14.271356783919598, 14.371859296482413, 14.472361809045227, 14.57286432160804, 14.673366834170855, 14.773869346733669, 14.874371859296483, 14.974874371859297, 15.075376884422111, 15.175879396984925, 15.27638190954774, 15.376884422110553, 15.477386934673367, 15.577889447236181, 15.678391959798995, 15.77889447236181, 15.879396984924623, 15.979899497487438, 16.080402010050253, 16.180904522613066, 16.28140703517588, 16.381909547738694, 16.48241206030151, 16.582914572864322, 16.683417085427138, 16.78391959798995, 16.884422110552766, 16.984924623115578, 17.085427135678394, 17.185929648241206, 17.286432160804022, 17.386934673366834, 17.48743718592965, 17.587939698492463, 17.68844221105528, 17.78894472361809, 17.889447236180906, 17.98994974874372, 18.090452261306535, 18.190954773869347, 18.291457286432163, 18.391959798994975, 18.49246231155779, 18.592964824120603, 18.69346733668342, 18.79396984924623, 18.894472361809047, 18.99497487437186, 19.095477386934675, 19.195979899497488, 19.296482412060303, 19.396984924623116, 19.49748743718593, 19.597989949748744, 19.69849246231156, 19.798994974874372, 19.899497487437188, 20.])
        yy = np.array([101.76405234596767, 99.99814715811596, 100.17471788360322, 101.03486304844768, 100.25951778914494, 97.0126718688673, 98.53802811601805, 97.0345724399435, 96.6807007461964, 96.79250804967705, 96.12394306864832, 97.03216295419915, 95.93691712213192, 94.89554436322649, 94.81572252922784, 94.30352357360542, 95.06191826913751, 92.96067088196284, 93.0768867971283, 91.5077133059244, 89.4068091791408, 92.21140754016398, 92.02021509333187, 90.01160382381465, 92.62151341795746, 88.49538306911982, 89.59349721076879, 88.95854479319024, 90.27649780732328, 89.81106731261384, 88.09464591815923, 87.91585096181322, 86.24789264432968, 84.75287187348461, 85.98374614213114, 86.08599721031, 86.7579288716825, 86.32800798948793, 84.33629127304431, 84.01930528962566, 82.87104502488266, 82.09757000251952, 81.40930769882223, 84.66434323442776, 81.80190560719308, 81.47147343708228, 80.25474232839228, 81.88301799402286, 79.08961974038175, 80.08876725747447, 79.00403092624352, 79.88438993504519, 78.58467224936581, 77.512835152561, 78.26327505809351, 78.31777910671131, 77.55395440831282, 77.38789903341817, 76.04909499174617, 75.91866586918874, 75.20693653714868, 75.11783377313282, 74.26223060237766, 72.94708423183917, 74.44878292617335, 73.46756579746007, 71.83713833645105, 73.5281088886916, 71.75601821853134, 72.31325192845945, 72.44768352700166, 71.04355577507901, 71.2499534483624, 68.07170684296293, 68.90485420399162, 67.01368237137123, 66.02367521262717, 65.5116025965421, 64.97487962867665, 64.53857740253125, 62.513242119015636, 63.77519834625066, 62.53601419852441, 59.730087972014225, 61.950563751584546, 61.55418063331701, 60.033050927943556, 57.87032642046905, 56.17547853426835, 57.49666278220751, 55.23501400780068, 56.05661592465378, 54.238425731845695, 54.202769689750035, 52.77847694993822, 52.32466362045325, 50.824570372479606, 51.79592074516211, 49.33294224345738, 48.80399941369595, 49.48114064680499, 45.44621078810378, 44.71946475025798, 46.15532635639921, 43.208786142624525, 45.521510632885466, 42.36025036597391, 41.22239443479039, 43.08877117220902, 41.84232383666055, 41.42534790515018, 39.65981350249648, 37.08852305866388, 39.055793596315105, 36.07370517176218, 36.34014483800745, 35.68092030948228, 33.77463814811519, 33.739707511049595, 33.24381471176753, 32.135219501004876, 30.257383129013792, 31.253012043552786, 31.879149715782503, 29.456185909112854, 29.59910917826529, 28.91158011662007, 30.793987346569793, 29.215008324851627, 28.54816535382905, 26.968777392891365, 27.87593260837724, 26.26034070617679, 26.564493874857263, 25.494807187952777, 26.4050765110269, 25.903223982444086, 24.71632435999989, 24.918619777988276, 23.027541506344868, 22.227335372118514, 23.7559746158374, 23.081246359694134, 23.147594250962456, 24.493697538683037, 22.65302220055825, 20.39371043787242, 22.02153890116118, 19.186605152302548, 19.6389179077481, 19.630250856986926, 21.009825133709665, 18.149717539760605, 17.66602377289877, 17.991999736881098, 17.024963924693168, 18.413068082910527, 15.80449060218934, 15.334943407890403, 15.642581965305816, 15.180359509106681, 17.205913963364722, 15.823792666222236, 14.559913050430415, 12.844916239963794, 14.512704684944259, 12.266116310901884, 11.319550511262587, 13.650341350141238, 12.377244119462537, 12.579150281067243, 11.575009059978196, 11.711101968686602, 9.801235713232515, 9.016008414496934, 10.329835724311778, 8.442821491605045, 8.154671327777438, 7.986678551759031, 8.057680164050181, 7.284197043520377, 5.861229611104593, 6.1905524514384584, 4.208757651795674, 6.655382204796024, 4.02608304791084, 4.121747313837874, 4.876285682276049, 3.6825475563724983, 5.563115097919298, 2.3252335425378505, 3.483131271359233, 2.774787533531291, 1.24396680376634, 2.533326911788028, 1.436493869782777, 1.977820701967429, 1.6275242544662438, 2.565245999531939, 1.336527949436392])

        # Choose some bps values from Muggeo converged values
        bps = np.array([7, 13])


        fit = Muggeo(xx, yy, n_breakpoints=2, start_values=bps, verbose=False)

        best_fit = fit.best_fit
        
        # Check statistics from breakpoints etc found by Muggeo
        # 1. MUggeo rss for these brreakpoints are 
        muggeo_rss = 190.02

        self.assertAlmostEqual(muggeo_rss, best_fit.residual_sum_squares, places=1)

        muggeo_c = 100.64655
        muggeo_c_se = 0.23081
        muggeo_c_t = 436.07

        muggeo_alpha = -4.18526
        muggeo_alpha_se = 0.05583
        muggeo_alpha_t = -74.97

        muggeo_beta1 = -3.65462
        muggeo_beta1_se = 0.11405
        muggeo_beta1_t = -32.05

        muggeo_beta2 = 3.81336
        muggeo_beta2_se = 0.11405
        muggeo_beta2_t = 34.45

        muggeo_bp1 = 7.152
        muggeo_bp1_se = 0.101

        muggeo_bp2 = 12.161
        muggeo_bp2_se = 0.095

        estimates = best_fit.estimates


        self.assertAlmostEqual(muggeo_c, estimates["const"]["estimate"], places=1)
        self.assertAlmostEqual(muggeo_alpha, estimates["alpha1"]["estimate"], places=1)
        self.assertAlmostEqual(muggeo_beta1, estimates["beta1"]["estimate"], places=1)
        self.assertAlmostEqual(muggeo_beta2, estimates["beta2"]["estimate"], places=1)
        self.assertAlmostEqual(muggeo_bp1, estimates["breakpoint1"]["estimate"], places=1)
        self.assertAlmostEqual(muggeo_bp2, estimates["breakpoint2"]["estimate"], places=1)

        self.assertAlmostEqual(muggeo_c_se, estimates["const"]["se"], places=1)
        self.assertAlmostEqual(muggeo_alpha_se, estimates["alpha1"]["se"], places=1)
        self.assertAlmostEqual(muggeo_beta1_se, estimates["beta1"]["se"], places=1)
        self.assertAlmostEqual(muggeo_beta2_se, estimates["beta2"]["se"], places=1)
        self.assertAlmostEqual(muggeo_bp1_se, estimates["breakpoint1"]["se"], places=1)
        self.assertAlmostEqual(muggeo_bp2_se, estimates["breakpoint2"]["se"], places=1)

        print(estimates)

        self.assertAlmostEqual(muggeo_c_t, estimates["const"]["t_stat"], delta=1)
        self.assertAlmostEqual(muggeo_alpha_t, estimates["alpha1"]["t_stat"], delta=1)
        self.assertAlmostEqual(muggeo_beta1_t, estimates["beta1"]["t_stat"], delta=1)
        self.assertAlmostEqual(muggeo_beta2_t, estimates["beta2"]["t_stat"], delta=1)

        muggeo_r_squared = 0.9991
        muggeo_adj_r_squared = 0.999

        self.assertAlmostEqual(muggeo_r_squared, best_fit.r_squared, places=2)
        self.assertAlmostEqual(muggeo_adj_r_squared, best_fit.adjusted_r_squared, places=2)

    def test_against_muggeo_r_package_data_2(self):
        """
        Muggeo uses slightly different packages and methods etc, so just check values are very close, not exact
        Starting from Muggeo's converged breakpoint values, I am iterating once, slight change
        The NextBreakpoint class is very vanilla, so in this example is getting in some local minima
        """

        xx = np.array([-9.5, -8.5, -7.5, -6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5,  0.5,
            1.5,  2.5,  3.5,  4.5,  5.5,  6.5,  7.5,  8.5,  9.5,  0. ,  0.5,
            1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,  5.5,  6. ,
            6.5,  7. ,  7.5,  8. ,  8.5,  9. ,  9.5])
        yy = np.array([-4.03710917, -3.13468604, -3.10145257, -1.49628907, -1.51588075,
            1.66277386,  2.5471815 ,  3.7002286 ,  3.89874821,  5.04199101,
            5.07523637,  7.0419681 ,  9.54622886, 11.23752194, 14.48493645,
           18.76995281, 19.50090828, 24.97803557, 24.48937084, 30.29809842,
            4.22530178,  5.18358577,  4.56814209,  5.62074975,  6.95089558,
            9.07815881,  9.66687336, 11.28907306, 12.58305054, 16.47828231,
           15.14445396, 19.51775633, 20.64684441, 21.2586812 , 21.25620389,
           23.25151255, 24.96582544, 25.88484136, 26.38244733, 29.7457742 ])

        # Choose some bps values from Muggeo converged values
        bps = np.array([1.608])

        fit = Muggeo(xx, yy, n_breakpoints=1, start_values=bps, verbose=False)

        best_fit = fit.best_fit

        # Check statistics from breakpoints etc found by Muggeo
        # 1. MUggeo rss for these brreakpoints are 
        muggeo_rss = 34.70127

        self.assertAlmostEqual(muggeo_rss, best_fit.residual_sum_squares, places=1)


        muggeo_c = 4.86206
        muggeo_c_se = 0.31020
        muggeo_c_t = 15.67

        muggeo_alpha = 0.94472
        muggeo_alpha_se = 0.06744
        muggeo_alpha_t = 14.01

        muggeo_beta1 = 1.95719
        muggeo_beta1_se = 0.11008
        muggeo_beta1_t = 17.78

        muggeo_bp1 = 1.608
        muggeo_bp1_se = 0.291

        estimates = best_fit.estimates


        self.assertAlmostEqual(muggeo_c, estimates["const"]["estimate"], places=1)
        self.assertAlmostEqual(muggeo_alpha, estimates["alpha1"]["estimate"], places=1)
        self.assertAlmostEqual(muggeo_beta1, estimates["beta1"]["estimate"], places=1)
        self.assertAlmostEqual(muggeo_bp1, estimates["breakpoint1"]["estimate"], places=1)
        
        self.assertAlmostEqual(muggeo_c_se, estimates["const"]["se"], places=1)
        self.assertAlmostEqual(muggeo_alpha_se, estimates["alpha1"]["se"], places=1)
        self.assertAlmostEqual(muggeo_beta1_se, estimates["beta1"]["se"], places=1)
        self.assertAlmostEqual(muggeo_bp1_se, estimates["breakpoint1"]["se"], places=1)
       
        self.assertAlmostEqual(muggeo_c_t, estimates["const"]["t_stat"], delta=1)
        self.assertAlmostEqual(muggeo_alpha_t, estimates["alpha1"]["t_stat"], delta=1)
        self.assertAlmostEqual(muggeo_beta1_t, estimates["beta1"]["t_stat"], delta=1)

        muggeo_r_squared = 0.9911
        muggeo_adj_r_squared = 0.9903

        self.assertAlmostEqual(muggeo_r_squared, best_fit.r_squared, places=2)
        self.assertAlmostEqual(muggeo_adj_r_squared, best_fit.adjusted_r_squared, places=2)


        





if __name__ == '__main__':
    unittest.main()
