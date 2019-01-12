from outrankingDigraphs import*
from perfTabs import *
from linearOrders import *
from sortingDigraphs import *
import xmcda

t = XMCDA2PerformanceTableau('project_1')

#t.showObjectives()
#t.showCriteria()
#t.showActions()
#t.showPerformanceTableau()
t.showHTMLPerformanceHeatmap(colorLevels=9)

teco = PartialPerformanceTableau(t, criteriaSubset=t.objectives['Eco']['criteria'])
teco.showHTMLPerformanceHeatmap(colorLevels=9)

tenv = PartialPerformanceTableau(t, criteriaSubset=t.objectives['Env']['criteria'])
tenv.showHTMLPerformanceHeatmap(colorLevels=9)

tsoc = PartialPerformanceTableau(t, criteriaSubset=t.objectives['Soc']['criteria'])
tsoc.showHTMLPerformanceHeatmap(colorLevels=9)

g = BipolarOutrankingDigraph(t)
g.showHTMLRelationTable()
geco = BipolarOutrankingDigraph(teco)
genv = BipolarOutrankingDigraph(tenv)
gsoc = BipolarOutrankingDigraph(tsoc)

### copeland
copg = CopelandOrder(g)
copg.showRanking()

copgeco = CopelandOrder(geco)
copgeco.showRanking()

copgenv = CopelandOrder(genv)
copgenv.showRanking()

copgsoc = CopelandOrder(gsoc)
copgsoc.showRanking()

### netflow
nfg = NetFlowsOrder(g)
nfg.showRanking()

nfgeco = NetFlowsOrder(geco)
nfgeco.showRanking()

nfgenv = NetFlowsOrder(genv)
nfgenv.showRanking()

nfgsoc = NetFlowsOrder(gsoc)
nfgsoc.showRanking()

### kohler
kog = KohlerOrder(g)
kog.showRanking()

kogeco = KohlerOrder(geco)
kogeco.showRanking()

kogenv = KohlerOrder(genv)
kogenv.showRanking()

kogsoc = KohlerOrder(gsoc)
kogsoc.showRanking()

###
qs_t = QuantilesSortingDigraph(t, 20)
qs_t.showSorting()
#qs_t.showQuantileOrdering()

qs_teco = QuantilesSortingDigraph(teco, 20)
qs_teco.showSorting()
#qs_teco.showQuantileOrdering()

qs_tenv = QuantilesSortingDigraph(tenv, 20)
qs_tenv.showSorting()
#qs_tenv.showQuantileOrdering()

qs_tsoc = QuantilesSortingDigraph(tsoc, 20)
qs_tsoc.showSorting()
#qs_tsoc.showQuantileOrdering()

### rubis
t_25 = PartialPerformanceTableau(t, actionsSubset=['a077', 'a069', 'a025', 'a036', 'a016', 'a072', 'a002', 'a007', 'a054', 'a058', 'a076', 'a040'])
g_25 = BipolarOutrankingDigraph(t_25)
g_25.showRubisBestChoiceRecommendation()

t_25eco = PartialPerformanceTableau(teco, actionsSubset=['a077', 'a069', 'a025', 'a036', 'a016', 'a072', 'a002', 'a007', 'a054', 'a058', 'a076', 'a040'])
g_25eco = BipolarOutrankingDigraph(t_25eco)
g_25eco.showRubisBestChoiceRecommendation()

t_25env = PartialPerformanceTableau(tenv, actionsSubset=['a077', 'a069', 'a025', 'a036', 'a016', 'a072', 'a002', 'a007', 'a054', 'a058', 'a076', 'a040'])
g_25env = BipolarOutrankingDigraph(t_25env)
g_25env.showRubisBestChoiceRecommendation()

t_25soc = PartialPerformanceTableau(tsoc, actionsSubset=['a077', 'a069', 'a025', 'a036', 'a016', 'a072', 'a002', 'a007', 'a024', 'a054', 'a058', 'a076', 'a040'])
g_25soc = BipolarOutrankingDigraph(t_25soc)
g_25soc.showRubisBestChoiceRecommendation()
###
gsoc.showPairwiseComparison('a077', 'a002')
gsoc.showPairwiseComparison('a077', 'a007')
gsoc.showPairwiseComparison('a077', 'a025')
gsoc.showPairwiseComparison('a077', 'a036')
gsoc.showPairwiseComparison('a077', 'a058')
gsoc.showPairwiseComparison('a077', 'a069')
gsoc.showPairwiseComparison('a077', 'a072')