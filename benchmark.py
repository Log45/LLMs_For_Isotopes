#from functions import *
import os

target_question = "What is the target material in the above reaction?"
acid_question = "What acid is the target material dissolved in during the above reaction?"
resin_question = "What resin/column is the solution loaded into during the above reaction?"
elution_question = "What acid is used in the elution during the above reaction?"
products_question = "What are the products of the above reaction?"

p1 = "Because both cobalt-55 and cobalt-58m require isolation from iron or nickel target materials, many of the radiochemical isolation processes reported can be applied to multiple production schemes. Several anion-exchange resins such as Dowex-2, Amberlite IRA-400, and ANEX-L have been historically used for the separation of Co from various transition metals in HCl, HNO3, and HBr solutions [94]."
q1 = (target_question, acid_question, resin_question, products_question)

p2 = "Previously reported separation methods to remove nickel from cobalt used the AG 1 × 8 anion-exchange resin [14,24]. These methods included the use of multiple grams of resin packed into a glass column and equilibrated with 9 M HCl. The dissolved target solution in 9M HCl was loaded onto the column where the nickel elutes from the column in the eluate and 9M HCl wash in 10–40 mL. The cobalt-5x, which remains on the column during the large 9M HCl wash, is eluted from the column in 10 mL of 0.1 M HCl. The eluted cobalt fraction can then be evaporated to dryness and reconstituted in various matrices for further analysis and/or radiolabeling experiments"
q2 = (target_question, acid_question, resin_question, elution_question, products_question)

p3 = "Anion-exchange chromatography also isolates cobalt-5x from iron target material [94]. After dissolving the target in acid, the iron is oxidized into the 3+ state with hydrogen peroxide. Instead of loading the cobalt-5x on to the anion-exchange resin and washing away the target material, as was performed in the nickel/cobalt anion-exchange separation, cobalt and iron are retained on the column when loaded. The cobalt can then be eluted form the anion-exchange column in 4 M HCl. The iron target will remain on the column during the 4 M HCl wash, but can be recovered in low concentrations of HCl. The HCl eluant containing cobalt-5x can also be evaporated and the cobalt-5x reconstituted in alternative matrices without incurring significant losses [26,28,86,87]."
q3 = (target_question, resin_question, elution_question, products_question)

p4 = "Separation of cobalt-5x from manganese is similar to the isolation of cobalt-5x from nickel targets, but can use even less concentrated acidic media. As summarized by Bate and Leddicotte in “The Radiochemistry of Cobalt”, manganese in a dissolved target solution passes through a AG1 × 8 anion-exchange resin in HCl concentrations > 4.5 HCl. Once the target material is removed, the column can be washed with <4.5 M HCl to elute cobalt-5x [94]."
q4 = (target_question, acid_question, resin_question, elution_question, products_question)

p5 = "As stated by Valdovinos et al., it is preferrable to use extraction chromatography instead of traditional ion exchange resins to increase separation yield and purity level [26]. This realization allowed for the implementation of N,N,N0 ,N0 -tetrakis-2-ethylhexyldiglycolamide (DGA Branched extraction resin). The most recent published separation methods from both nickel and iron targets of varying enrichments use branched DGA to chemically isolate radioactive cobalt."
q5 = (target_question, resin_question, products_question)

p6 = "The newer separation method for separating nickel from cobalt is straightforward, using one column containing branched DGA resin, as shown in Figure 17."
q6 = (target_question, resin_question, products_question)

p7 = "The separation of cobalt-5x from iron-5x uses a two column technique, as shown in Figure 18. An AG1X8 anion-exchange resin packed column is used for the bulk separation of iron and cobalt, then a DGA column serves as a “clean up” to further improve the purification of cobalt-5x [26]."
q7 = (target_question, resin_question, products_question)

p8 = "While there has not been a publication specifically on the separation of manganese target material from cobalt-55,58m, the work performed by Pourmand et al. suggests branched DGA can also be used for radio-chemical isolation using 4–6 M HCl, where in this range manganese 2+ has minimal affinity for the resin, and cobalt 2+ has a greater affinity [95]."
q8 = (target_question, acid_question, resin_question, products_question)

p9 = "While not widely used for radiochemistry, early studies showed that cobalt can be separated from iron 3+ and nickel 2+ with the use of inorganic and organic absorbents [94]. Many of the inorganic separations were using alumina, a polar column chromatography absorbent [96]. The organic separations from iron 2+ and nickel 2+ rely on columns of 8-hydroxyquinoline, naphthaquinoline, and cupferron mixed with potato starch or dimethylglyoxime compound columns, as reported by Bate and Leddicotte, [94]."
q9 = (target_question, resin_question, products_question)

p10 = "In order to make 64Cu via the nuclear reaction of 64Ni (p, n) 64Cu, we made the enriched 64Ni targets on a gold (Au) disk by electrodeposition of 64Ni from an aqueous solution of Ni(NH3)6 2+ at pH = 9.05, using a robust, reliable and user-friendly apparatus (Figure 1). The Au disk (30.8 mm diameter × 1.5 mm thickness) was used as a cathode, and a platinum wire was used as an anode. A cavity of 12.1 mm diameter and 0.2 mm depth was milled into the Au disk and 64Ni (99.32%) was plated into this cavity. The 64Ni electroplating was performed with a constant current of 15–25 mA at 2.4–2.6 V in the aqueous solution for 48–72 h. During the electrodeposition, the green color of the 64Ni plating solution gradually faded away and the bubbling of H2 gas was clearly visible. When the 64Ni plating solution became colorless, the electrodeposition was finished. The absence of Ni2+ was also confirmed by analytical test strips. After cleaning and drying, the plated 64Ni on Au-disk was 70.6 ± 5.8 mg and the density of the plated 64Ni was 61.4 ± 5.0 mg/cm2 , assuming a uniform thickness on the disk."
q10 = (target_question)

p11 = "After irradiation of 5 h, the 64Ni target was dissolved in 6 M hydrochloride acid, and then the solution was load to an anion exchange column to separate into different components. The 64Ni was washed out with 6 M HCl and collected for recycling. Due to the elevated cost of enriched 64Ni, recycling of the target material for re-use could reduce the production cost of 64Cu, without sacrificing the quality of subsequent 64Cu production. When the eluted was switched to 1 M HCl, the first band coming out was co-produced cobalt radioisotopes (approximately 1 mL), and the second was the 64Cu, which was collected and evaporated to dryness. The residue was dissolved in 0.1 M HCl for further use. The separation process of 64Cu took about 2.5 h after irradiation"
q11 = (target_question, acid_question, resin_question, elution_question, products_question)

p12 = "After irradiation, the 64Ni target was placed into the dissolving bath of 6 M HCl. The complete dissolution of the target material took about 40 min under heating, and then the solution was loaded on an anion exchange column (AG 1-X8) pretreated with 18 MΩ·cm water and 6 M HCl, sequentially. The enriched 64Ni was eluted with 6 M HCl and collected for recycling, and the 64Cu fraction was eluted with 1 M HCl, which was further evaporated to dryness. The residue was finally dissolved in 0.1 M HCl for further use. All of these procedures were performed using an automated system and carried out in a hot cell with remote control (Figure 7, Sumitomo Heavy Industries, Ltd., Tokyo, Japan)"
q12 = (target_question, acid_question, resin_question, elution_question, products_question)

p13 = "The purified 228Ac preparation was obtained in several stages. In the fi rst stage, macroamounts 232Th and accumulated 228Th are separated from a mixture of their decay products (Fig. 1) via extraction of thorium by a 1 : 1 solution of di(2-ethylhexyl)phosphoric acid (HDEHP) in toluene from 4 M HNO3 solutions. The choce of the extraction agent was governed by earlier studies [4] in which it was found that the best reagent among those examined for separation of 232Th from products formed in its irradiation by high-energy protons (and also of radium and actinium) is HDEHP, which extracts 232Th from nitrate solutions in a wide range of HNO3 concentrations [25–27]. The phases were vigorously agitated for 5 min, centrifuged, and then separated in a separating funnel. The extraction was performed three times, and the aqueous solution with 228Ra was passed, to be fuller purifi ed to remove thorium, through a column with extraction-chromatographic sorbent LN (Triskem Int., France, based on HDEHP, particles size 100–150 mesh). The sorbent fi rmly retains thorium in a wide range of HNO3 concentrations, with radium and actinium not retained by this sorbent at HNO3 concentrations exceeding 0.2 M [28]."
q13 = (target_question, acid_question, resin_question, products_question)

p14 = "The mixture of nuclides, remaining after the separation of thorium isotopes contains 228Ra (in which 228Ac accumulates) and also 224Ra (in equilibrium with other decay products, including gaseous 220Rn) and the stable 208Pb. A single-stage isolation of 228Ac from a mixture of this kind is a complicated task, and deep purifi cation to remove 224Ra is necessary for obtaining the radiochemically pure 228Ac. For this reason, the mixture was kept for one month till the complete decay of 224Ra. In the fi nal stage, 228Ac was separated from 228Ra, 208Pb, and newly formed 228Th. For this purpose, a solution of 228Ra in HNO3 was evaporated to dryness in a glass fl ask on an electric hot plate, dissolved in 4 M HNO3; and the solution was placed in a column with RE extraction-chromatographic sorbent (Triskem Int., France, based on carbamoylmethylphosphine oxide and tributyl phosphate) with volume of 2 mL. 228Ra and 228Ac were separated by selective elution from the column: fi rst, 228Ra was eluted with a 4 M HNO3 solution, and then 228Ac, in 0.05 M HNO3, with fractions collected each having a volume of 1 mL The purity of 228Ac was determined by registering its gammaspectrum during three days. To perform experiments on sorption of actinium on CNMs, the 228Ac eluate in 0.05 M HNO3 was evaporated to dryness and dissolved in several mL of a phosphate buff ered saline (PBS) with pH 7"
q14 = (target_question, acid_question, resin_question, elution_question, products_question)

p15 = "Development of a procedure for separation of radiochemically pure 228Ac from natural thorium. It was shown that 228,232Th is extracted with HDEHP from a 4 M HNO3 solution nearly quantitatively (99%), with no 228Ra extracted in this case. An additional purifi cation of 228Ra remaining in the aqueous phase to remove thorium was performed by its passing through a column with extraction-chromatographic sorbent LN, with 99.9% 228Ra and not more than 0.01% 228,232Th contained in the eluate. 228Ra and 228Ac were separated by the extraction-chromatographic method on the RE sorbent. It can be seen in Fig. 2, which shows a chromatogram, that 228Ra is quantitatively extracted in 2–5-mL fractions and 228Ac in 13–16-mL fractions. The fl ow rate of the eluate was 1 mL/min, which makes it possible to separate 228Ra and 228Ac in 20 min. It was found here that the yield of 228Ac is nearly quantitative (not less than 95% relative to the amount placed on the column), with the separation factor of 228Ra and 228Ac being 2.2 × 104. According to [31], 208Pb is eluted from the column together with 228Ra. Thus, we developed a method for separation 228Ac in the radiochemically pure state from large amounts of natural thorium. The isolated 228Ac can be used in scientifi c studies, including in vivo experiments."
q15 = (target_question, acid_question, resin_question, products_question)

p16 = "It was found that, with the developed method implemented, the loss of 228Ra does not exceed 0.005% of the amount placed in the column. Therefore, the starting 228Ra preparation can be repeatedly used. For this purpose, the fractions from 1 to 9 mL were evaporated and again dissolved in 1 mL of 4 M HNO3. It was shown that the results are reproducible because 228Ac could be eluted from the generator we developed not less than 20 times. In a prolonged use of the solution of 228Ra, there occurs accumulation of 228Th occurs due to the decay of 228Ac, but 228Th is quantitatively sorbed on the column with RE in the process of separation of 228Ra and 228Ac [31]. It is supposed that the columns with the sorbent are intended for single use, and, therefore, 228Th does not contaminate the solution of 228Ac being prepared. In the many-years use of the generator, the extract of 232Th can be repeatedly used to extract 228Ra accumulated in it."
q16 = (target_question, acid_question, products_question)

relevant_contexts = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]
paragraph_questions_dict = {p1:q1, p2:q2, p3:q3, p4:q4, p5:q5, p6:q6, p7:q7, p8:q8, p9:q9, p10:q10, p11:q11, p12:q12, p13:q13, p14:q14, p15:q15, p16:q16}
   
def find_paragraph(s: set, context:list):
    """_summary_

    Args:
        s (set): _description_
        context (list): _description_
    """
    test_sets = []
    test_set_dict = {}
    # Convert every context paragraph to a set of words
    for t in context:
        test_sets.append(set(t.split()))
        test_set_dict[t] = set(t.split())
        
    l = len(s)
    overlap = []
    for s1 in test_sets:
        # Find intersection of the initial set and the specific set from the list of contexts
        inter = s1.intersection(s)
        l1 = len(inter)
        # Ensure that the context set matches 65% of the target set
        if (l1/l) >= .65:
            for t in context:
                if len(s1.intersection(test_set_dict[t])) == len(test_set_dict[t]):
                    if(len(t)) > 2:
                        overlap.append(t)
    relevant = overlap[0] if len(overlap) > 0 else ""
    # Sort out weird outlier matches
    for c in overlap:
        if len(c) > len(relevant):
            relevant = c
    overlap = [relevant]
    # Return the relevant paragraph (that has the most matching elements of target set)
    return relevant


def find_relevant_paragraphs(relevant_contexts: list, context: list):
    """_summary_

    Args:
        relevant_contexts (list): _description_
        context (list): _description_
    """
    context_set_dict = {}
    relevant_sets = []
    
    for c in relevant_contexts:
        relevant_sets.append(set(c.split()))
        context_set_dict[c] = set(c.split())
    
    paragraphs = []
    response_context_dict = {}
    for s in relevant_sets:
        i = relevant_sets.index(s)
        paragraph = find_paragraph(s, context)
        paragraphs.append(paragraph)
        response_context_dict[paragraph] = relevant_contexts[i]
    return response_context_dict


def extract_context(filepath:str):
    """_summary_

    Args:
        filename (str): _description_
    """
    context = []
    with open(filepath, encoding="UTF-8") as file:
        context_counter = 0
        for line in file:
            if "Context: " in line:
                context_counter += 1
                idx = line.index("Context: ")
                context.append(line[idx+9:].strip())
    return context


def extract_context_qna(filepath: str):
    """_summary_

    Args:
        filepath (str): _description_
    """
    contexts = []
    context_qna_dict = {}
    with open(filepath, "r", encoding="UTF-8") as file:
        ofile = file.readlines()
        f = ""
        for line in ofile:
            f+=line
        
        sections = f.split("Con")
        
    
        for section in sections:
            c = ""
            q = ""
            a = ""
            qna = []
            lines = section.split("\n")
            for line in lines:
                
                if "text: " in line:
                    contexts.append(line[len("text: "):].strip())
                    c = line[len("text: "): ].strip()
                    
                elif "Question: " in line:
                    q = line[len("Question: "):].strip()
                   
                elif "Answer:" in line:
                    a = line[len("Answer:"):].strip()

                if c != "" and a != "" and q !="":
                    qc = q
                    ac = a
                    qna = qna + [(qc, ac)]
                    qnac = qna
                    context_qna_dict[c] = qnac
                    q = ""
                    a = ""
    return context_qna_dict          


def run_benchmark():
    """"""   
    directory = "output" 
    output_list = []
    for name in os.listdir(directory):
        d = os.path.join(directory, name)
        if os.path.isdir(d):
            for file in os.listdir(d):
                f = os.path.join(d, file)
                if ".out" in file or "placeholder" in file:
                    pass
                else:
                    if os.path.isfile(f):
                        generations, time, perp_score = get_stats(f)
                        score = 0
                        context = extract_context(f)
                        context_qna_dict = extract_context_qna(f)
                        if "html" in f:
                            total_points = 45
                            r_contexts = relevant_contexts[:-4]
                            response_context_dict = find_relevant_paragraphs(r_contexts, context)
                        else:
                            total_points = 61
                            response_context_dict = find_relevant_paragraphs(relevant_contexts, context)
                        relevant_tracker = 0
                        for c in context:
                            relevant_context = response_context_dict[c] if c in response_context_dict.keys() else None
                            qna = context_qna_dict[c] if c in context_qna_dict.keys() else None
                            if relevant_context is not None and qna is not None:
                                for tup in qna:
                                    q = tup[0]
                                    a = tup[1]
                                    paragraph_questions = paragraph_questions_dict[relevant_context]
                                    if q in paragraph_questions:
                                        relevant_tracker+=1
                                        # Make conditions for each question and answer and add to score if has certain parts in the string
                                        if relevant_context == p1:
                                            if q == target_question:
                                                if "Iron" in a or "iron" in a or "Fe" in a:
                                                    score+=0.5
                                                if "Nickel" in a or "nickel" in a or "Ni" in a:
                                                    score+=0.5
                                            elif q == acid_question:
                                                if "HCl" in a:
                                                    score+=0.34
                                                if "HNO3" in a:
                                                    score+=0.33
                                                if "HBr" in a:
                                                    score+=0.33
                                            elif q == resin_question:
                                                if "Dowex-2" in a:
                                                    score+=0.34
                                                if "Amberlite IRA-400" in a:
                                                    score+=0.33
                                                if "ANEX-L" in a:
                                                    score+=0.33
                                            elif q == products_question:
                                                if "cobalt-55" in a or "Cobalt-55" in a or "55Co" in a:
                                                    score+=0.5
                                                if "cobalt-58m" in a or "Cobalt-58m" in a or "58mCo" in a:
                                                    score+=0.5
                                        elif relevant_context == p2:
                                            if q == target_question:
                                                if "nickel" in a or "Nickel" in a:
                                                    score+=1
                                            elif q == acid_question:
                                                if "9M HCl" in a or "9 M HCl" in a or ("9M" in a and "HCl" in a):
                                                    score+=1
                                            elif q == resin_question:
                                                if "AG 1 × 8" in a or "AG1×8" in a or "AG 1×8" in a or ("AG" in a and "anion-exchange resin" in a):
                                                    score+=1
                                            elif q == elution_question:
                                                if "0.1M HCl" in a or "0.1 M HCl" in a:
                                                    score+=1
                                            elif q == products_question:
                                                if "cobalt" in a or "Cobalt" in a or "Co" in a:
                                                    score+=1
                                        elif relevant_context == p3:
                                            if q == target_question:
                                                if "Iron" in a or "iron" in a or "Fe" in a:
                                                    score+=1
                                            elif q == resin_question:
                                                if "anion-exchane" in a or "Anion-exchange" in a:
                                                    score+=1
                                            elif q == elution_question:
                                                if "4M HCl" in a or "4 M HCl" in a:
                                                    score+=1
                                            elif q == products_question:
                                                if "cobalt-5x" in a or "Cobalt-5x" in a or "5xCo" in a:
                                                    score+=1
                                        elif relevant_context == p4:
                                            if q == target_question:
                                                if "manganese" in a or "Manganese" in a or "Mn" in a:
                                                    score+=1
                                            elif q == acid_question:
                                                if ">" in a:
                                                    score+=0.5
                                                if "4.5M HCl" in a or "4.5 M HCl" in a:
                                                    score+=0.5
                                            elif q == resin_question:
                                                if "anion-exchange" in a or "Anion-exchange" in a:
                                                    score+=0.5
                                                if "AG1 × 8 " in a or ("AG" in a and "1" in a and "8" in a):
                                                    score+=0.5
                                            elif q == elution_question:
                                                if "<" in a:
                                                    score+=0.5
                                                if "4.5M HCl" in a or "4.5 M HCl" in a:
                                                    score+=0.5 
                                            elif q == products_question:
                                                if "Cobalt-5x" in a or "cobalt-5x" in a or "5xCo" in a:
                                                    score+=1
                                        elif relevant_context == p5:
                                            if q == target_question:
                                                if "Nickel" in a or "nickel" in a or "Ni" in a:
                                                    score+=0.5
                                                if "Iron" in a or "iron" in a or "Fe" in a:
                                                    score+=0.5
                                            elif q == resin_question:
                                                if "N,N,N0 ,N0 -tetrakis-2-ethylhexyldiglycolamide" in a or "DGA Branched extraction resin" in a or ("DGA" in a and "resin" in a) or ("DGA" in a and "branched" in a):
                                                    score+=1
                                            elif q == products_question:
                                                if "radioactive cobalt" in a or "Radioactive cobalt" in a or "Radioactive Cobalt" in a:
                                                    score+=1
                                        elif relevant_context == p6:
                                            if q == target_question:
                                                if "nickel" in a or "Nickel" in a or "Ni" in a:
                                                    score+=1
                                            elif q == resin_question:
                                                if "DGA" in a and ("branched" in a or "Branched" in a):
                                                    score+=1
                                            elif q == products_question:
                                                if "cobalt" in a or "Cobalt" in a or "Co" in a:
                                                    score+=1
                                        elif relevant_context == p7:
                                            if q == target_question:
                                                if "iron-5x" in a or "Iron-5x" in a or "5xFe" in a:
                                                    score+=1
                                            elif q == resin_question:
                                                if "AG1X8" in a:
                                                    score+=0.5
                                                if "DGA" in a:
                                                    score+=0.5
                                            elif q == products_question:
                                                if "cobalt-5x" in a or "Cobalt-5x" in a or "5xCo" in a:
                                                    score+=1
                                        elif relevant_context == p8:
                                            if q == target_question:
                                                if "manganese" in a or "Manganese" in a or "Mn" in a:
                                                    score+=1
                                            elif q == acid_question:
                                                if ("4–6 M" in a or "4–6M" in a) and "HCl" in a:
                                                    score+=1
                                            elif q == resin_question:
                                                if "DGA" in a and ("branched" in a or "Branched" in a):
                                                    score+=1
                                            elif q == products_question:
                                                if "cobalt-55" in a or "Cobalt-55" in a or "55Co" in a:
                                                    score+=0.5
                                                if "cobalt-58m" in a or "Cobalt-58m" in a or "58mCo" in a:
                                                    score+=0.5
                                        elif relevant_context == p9:
                                            if q == target_question:
                                                if "Iron" in a or "iron" in a or "Fe" in a:
                                                    score+=0.5
                                                if "Nickel" in a or "nickel" in a or "Ni" in a:
                                                    score+=0.5
                                            elif q == resin_question:
                                                if "alumina" in a or "Alumina" in a:
                                                    score+=0.25
                                                if "8-hydroxyquinoline" in a:
                                                    score+=0.25
                                                if "naphthaquinoline" in a:
                                                    score+=0.25
                                                if "cupferron" in a and ("potator starch" in a or "dimethylglyoxime" in a):
                                                    score+=0.25
                                            elif q == products_question:
                                                if "Cobalt" in a or "cobalt" in a or "Co" in a:
                                                    score+=1
                                        elif relevant_context == p10:
                                            if q == target_question:
                                                if "Nickel-64" in a or "nickel-64" in a or "64Ni" in a:
                                                    score+=1
                                        elif relevant_context == p11:
                                            if q == target_question:
                                                if "Nickel-64" in a or "nickel-64" in a or "64Ni" in a:
                                                    score+=1
                                            elif q == acid_question:
                                                if "6 M HCl" in a or "6M HCl" in a or "6 M hydrochloride acid" in a:
                                                    score+=1
                                            elif q == resin_question:
                                                if "anion exchange" in a or "Anion exchange" in a or "Anion Exchange" in a:
                                                    score+=1
                                            elif q == elution_question:
                                                if "1 M HCl" in a or "1M HCl" in a:
                                                    score+=1
                                            elif q == products_question:
                                                if "Copper-64" in a or "copper-64" in a or "64Cu" in a:
                                                    score+=0.5
                                                if "cobalt" in a or "Cobalt" in a:
                                                    score+=0.5
                                        elif relevant_context == p12:
                                            if q == target_question:
                                                if "Nickel-64" in a or "nickel-64" in a or "64Ni" in a:
                                                    score+=1
                                            elif q == acid_question:
                                                if "6 M HCl" in a or "6M HCl" in a or "6 M hydrochloride acid" in a:
                                                    score+=1
                                            elif q == resin_question:
                                                if "anion exchange" in a or "Anion exchange" in a or "Anion Exchange" in a:
                                                    score+=0.5
                                                if "AG 1-X8" in a or "AG 1" in a:
                                                    score+=0.5
                                            elif q == elution_question:
                                                if "1 M HCl" in a or "1M HCl" in a:
                                                    score+=1
                                            elif q == products_question:
                                                if "Copper-64" in a or "copper-64" in a or "64Cu" in a:
                                                    score+=0.5
                                        elif relevant_context == p13:
                                            if q == target_question:
                                                if "Thorium" in a or "thorium" in a or "Th" in a:
                                                    score+=0.5
                                                if "232" in a:
                                                    score+=0.25
                                                if "228" in a:
                                                    score+=0.25
                                            elif q == acid_question:
                                                if "di(2-ethylhexyl)phosphoric" in a or "HDEHP" in a:
                                                    score+=0.5
                                                if "4 M HNO3" in a or "4M HNO3" in a:
                                                    score+=0.5
                                            elif q == resin_question:
                                                if "chromatographic sorbent" in a or "LN" in a:
                                                    score+=1
                                            elif q == products_question:
                                                if "Actinium-228" in a or "actinium-228" in a or "228Ac" in a:
                                                    score+=1
                                        elif relevant_context == p14:
                                            if q == target_question:
                                                if "Radium-228" in a or "radium-228" in a or "228Ra" in a:
                                                    score+=0.34
                                                if "Lead-208" in a or "lead-208" in a or "208Pb" in a:
                                                    score+=0.33
                                                if "Thorium-228" in a or "thorium-228" in a or "228Th" in a:
                                                    score+=0.33
                                            elif q == acid_question:
                                                if "4 M HNO3" in a or "4M HNO3" in a:
                                                    score+=1
                                            elif q == resin_question:
                                                if "RE" in a or "chromatographic sorbent" in a:
                                                    score+=1
                                            elif q == elution_question:
                                                if "0.05 M HNO3" in a or "0.05M HNO3" in a:
                                                    score+=1
                                            elif q == products_question:
                                                if "Actinium-228" in a or "actinium-228" in a or "228Ac" in a:
                                                    score+=1
                                        elif relevant_context == p15:
                                            if q == target_question:
                                                if "Thorium" in a or "thorium" in a or "Th" in a:
                                                    score+=0.5
                                                if "Radium-228" in a or "radium-228" in a or "228Ra" in a:
                                                    score+=0.5
                                            elif q == acid_question:
                                                if "4 M HNO3" in a or "4M HNO3" in a:
                                                    score+=1
                                            elif q == resin_question:
                                                if "RE" in a or "chromatographic sorbent" in a:
                                                    score+=1
                                            elif q == products_question:
                                                if "Actinium-228" in a or "actinium-228" in a or "228Ac" in a:
                                                    score+=1
                                        elif relevant_context == p16:
                                            if q == target_question:
                                                if "Radium-228" in a or "radium-228" in a or "228Ra" in a:
                                                    score+=1
                                            elif q == acid_question:
                                                if "4 M HNO3" in a or "4M HNO3" in a:
                                                    score+=1
                                            elif q == products_question:
                                                if "Actinium-228" in a or "actinium-228" in a or "228Ac" in a:
                                                    score+=1
                    parser = "html" if "html" in f else "pdf"
                    ratio = round(score/total_points, 2)
                    generations = int(generations)
                    time = float(time)
                    # Tuple format:
                    # filename, score, total generations, total time, efficiency (gen/min), perplexity score, relevant generations, percent of relevent generations generated, wasted generations, parser
                    output_list.append((f[len("output/"):],ratio, generations, time, (generations/time)*60, perp_score, relevant_tracker, relevant_tracker/total_points, generations-relevant_tracker, parser))
    return output_list


def get_stats(filepath):
    """_summary_

    Args:
        file (_type_): _description_
    """
    with open(filepath, "r", encoding="UTF-8") as file:
        line = file.readline()
        generations = line[line.index("Generated ")+10: line.index(" responses")]
        time = line[line.index("in ")+3: line.index(" seconds")]
        if "initial" not in filepath:
            perp_score = 0
        else:
            perp_score = line[line.index("of ")+3: line.index("\n")]
        return (generations, time, perp_score)


def write_to_csv():
    """_summary_
    """
    output_list = run_benchmark()
    with open("results.csv", "w", encoding="UTF-8") as f:
        f.write("filename,score,total generations,total time,efficiency (gen/min),perplexity score,relevant generations,percent of relevant generations generated,wasted generations,parser\n")
        for tup in output_list:
            # Tuple format:
            # filename, score, total generations, total time, efficiency (gen/min), perplexity score, relevant generations, percent of relevant generations generated, wasted generations, parser
            filename, score, generations, time, efficiency, perplexity, relevent_gens, percent_relevant, wasted_gens, parser = tup
            filename = filename.replace("\ ", "/")
            if "fourth_test" in filename and "-2" in filename:
                pass
            else:
                f.write(f"{filename},{score},{generations},{time},{efficiency},{perplexity},{relevent_gens},{percent_relevant},{wasted_gens},{parser}\n")
            
write_to_csv()