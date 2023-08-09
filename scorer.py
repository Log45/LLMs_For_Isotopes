"""
Sorry for the spaghetti-code:
This file goes through the results.csv file and extracts the accuracy, efficiency, perplexity, and wastefulness of 
each file and calculates the average with regards to the model, the filter, and the prompt used. 

Author: Logan Endes @Log45 on github
"""

import matplotlib.pyplot as plt

with open("results.csv", "r", encoding="UTF-8") as f:
    output_lst = []
    model_dict = {}
    falcon = []
    gal_7 = []
    gal_1 = []
    l_7 = []
    l_13 = []
    zero = []
    one = []
    two = []
    kf = []
    mf = []
    km = []
    kmc = []
    kme = []
    kmec = []
    for line in f:
        if "filename" in line:
            pass
        else:
            #filename,score,total generations,total time,efficiency (gen/min),perplexity score,relevant generations,percent of relevant generations generated,wasted generations,parser
            name, acc, gens, time, eff, perp, relgen, percrelgen, wasted, parser = line.strip().split(",")
            print(perp)
            output_lst.append((name, acc, gens, time, eff, perp, relgen, percrelgen, wasted, parser))
            model_dict[name] = (acc, eff, perp, int(wasted)/int(gens))
            # classify by models
            if "13b" in name:
                l_13.append(name)
            elif "2-7b" in name:
                l_7.append(name)
            elif "n-7b" in name:
                falcon.append(name)
            elif "1.3" in name:
                gal_1.append(name)
            elif "6.7" in name:
                gal_7.append(name)
            # classify by prompt
            if "-0" in name:
                zero.append(name)
            elif "-1.txt" in name:
                one.append(name)
            elif "-2.txt" in name:
                two.append(name)
            # classify by filter
            if "keyword_filter" in name:
                kf.append(name)
            elif "model_filter" in name:
                mf.append(name)
            elif "model_check" in name:
                kmc.append(name)
            elif "model_expert_generate" in name:
                kme.append(name)
            elif "model_expert_check" in name:
                kmec.append(name)
            elif "keyword_model_gen" in name:
                km.append(name)

model_acc = {}
model_eff = {}
model_perp = {}
model_wasted = {}

acc = 0
eff = 0
perp = 0
waste = 0
for output in l_13:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    perp += float(model_dict[output][2])
    waste += float(model_dict[output][3])
model_acc["LLaMA-2-13b"] = round(acc/len(l_13), 2)
model_eff["LLaMA-2-13b"] = round(eff/len(l_13), 2)
model_perp["LLaMA-2-13b"] = round(perp/len(l_13), 2)
model_wasted["LLaMA-2-13b"] = round(waste/len(l_13), 2)

acc = 0
eff = 0
perp = 0
waste = 0
for output in l_7:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    perp += float(model_dict[output][2])
    waste += float(model_dict[output][3])
model_acc["LLaMA-2-7b"] = round(acc/len(l_7), 2)
model_eff["LLaMA-2-7b"] = round(eff/len(l_7), 2)
model_perp["LLaMA-2-7b"] = round(perp/len(l_7), 2)
model_wasted["LLaMA-2-7b"] = round(waste/len(l_7), 2)

acc = 0
eff = 0
perp = 0
waste = 0
for output in gal_7:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    perp += float(model_dict[output][2])
    waste += float(model_dict[output][3])
model_acc["Galactica-6.7b"] = round(acc/len(gal_7), 2)
model_eff["Galactica-6.7b"] = round(eff/len(gal_7), 2)
model_perp["Galactica-6.7b"] = round(perp/len(gal_7), 2)
model_wasted["Galactica-6.7b"] = round(waste/len(gal_7), 2)


acc = 0
eff = 0
perp = 0
waste = 0
for output in gal_1:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    perp += float(model_dict[output][2])
    waste += float(model_dict[output][3])
model_acc["Galactica-1.3b"] = round(acc/len(gal_1), 2)
model_eff["Galactica-1.3b"] = round(eff/len(gal_1), 2)
model_perp["Galactica-1.3b"] = round(perp/len(gal_1), 2)
model_wasted["Galactica-1.3b"] = round(waste/len(gal_1), 2)


acc = 0
eff = 0
perp = 0
waste = 0
for output in falcon:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    perp += float(model_dict[output][2])
    waste += float(model_dict[output][3])
if len(falcon) > 0:
    model_acc["Falcon-7b"] = round(acc/len(falcon), 2)
    model_eff["Falcon-7b"] = round(eff/len(falcon), 2)
    model_perp["Falcon-7b"] = round(perp/len(falcon), 2)
    model_wasted["Falcon-7b"] = round(waste/len(falcon), 2)
else:
    model_acc["Falcon-7b"] = 0
    model_eff["Falcon-7b"] = 0
    model_perp["Falcon-7b"] = 0
    model_wasted["Falcon-7b"] = 0

model_labels = ["Galactica-1.3b", "Galactica-6.7b", "Falcon-7b", "LLaMA-2-7b", "LLaMA-2-13b"]
model_acc_h = [model_acc["Galactica-1.3b"], model_acc["Galactica-6.7b"], model_acc["Falcon-7b"], model_acc["LLaMA-2-7b"], model_acc["LLaMA-2-13b"]]
model_eff_h = [model_eff["Galactica-1.3b"], model_eff["Galactica-6.7b"], model_eff["Falcon-7b"], model_eff["LLaMA-2-7b"], model_eff["LLaMA-2-13b"]]
model_perp_h = [model_perp["Galactica-1.3b"], model_perp["Galactica-6.7b"], model_perp["Falcon-7b"], model_perp["LLaMA-2-7b"], model_perp["LLaMA-2-13b"]]
model_wasted_h = [model_wasted["Galactica-1.3b"], model_wasted["Galactica-6.7b"], model_wasted["Falcon-7b"], model_wasted["LLaMA-2-7b"], model_wasted["LLaMA-2-13b"]]


plt_acc = plt.bar([2*i for i in range(len(model_labels))], model_acc_h, tick_label=model_labels)
plt.ylabel("Accuracy")
plt.title("Accuracy by Model")
plt.savefig('model_accuracy.png')
plt.close()

plt_eff = plt.bar([2*i for i in range(len(model_labels))], model_eff_h, tick_label=model_labels)
plt.ylabel("Efficiency (Gen/Min)")
plt.title("Efficiency by Model")
plt.savefig('model_efficiency.png')
plt.close()

plt_perp = plt.bar([2*i for i in range(len(model_labels))], model_perp_h, tick_label=model_labels)
plt.ylabel("Perplexity")
plt.title("Perplexity by Model")
plt.savefig('model_perplexity.png')
plt.close()

print(model_perp_h, model_perp)
plt_waste = plt.bar([2*i for i in range(len(model_labels))], model_wasted_h, tick_label=model_labels)
plt.ylabel("% Wasted Generations")
plt.title("% Wastefulness by Model")
plt.savefig('model_waste.png')
plt.close()

filter_acc = {}
filter_eff = {}
filter_wasted = {}

acc = 0
eff = 0
waste = 0
for output in kf:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    waste += float(model_dict[output][3])
filter_acc["K"] = round(acc/len(kf), 2)
filter_eff["K"] = round(eff/len(kf), 2)
filter_wasted["K"] = round(waste/len(kf), 2)

acc = 0
eff = 0
waste = 0
for output in mf:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    waste += float(model_dict[output][3])
filter_acc["M"] = round(acc/len(mf), 2)
filter_eff["M"] = round(eff/len(mf), 2)
filter_wasted["M"] = round(waste/len(mf), 2)

acc = 0
eff = 0
waste = 0
for output in km:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    waste += float(model_dict[output][3])
if len(km)!=0:
    filter_acc["KM"] = round(acc/len(km), 2)
    filter_eff["KM"] = round(eff/len(km), 2)
    filter_wasted["KM"] = round(waste/len(km), 2)


acc = 0
eff = 0
waste = 0
for output in kmc:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    waste += float(model_dict[output][3])
if len(kmc) !=0:
    filter_acc["KMC"] = round(acc/len(kmc), 2)
    filter_eff["KMC"] = round(eff/len(kmc), 2)
    filter_wasted["KMC"] = round(waste/len(kmc), 2)
else:
    filter_acc["KMC"] = 0
    filter_eff["KMC"] = 0
    filter_wasted["KMC"] = 0

acc = 0
eff = 0
waste = 0
for output in kme:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])
    waste += float(model_dict[output][3])
if len(kme) > 0:
    filter_acc["KME"] = round(acc/len(kme), 2)
    filter_eff["KME"] = round(eff/len(kme), 2)
    filter_wasted["KME"] = round(waste/len(kme), 2)
else:
    filter_acc["KME"] = 0
    filter_eff["KME"] = 0
    filter_wasted["KME"] = 0

acc = 0
eff = 0
waste = 0
for output in kmec:
    acc += float(model_dict[output][0])
    eff += float(model_dict[output][1])

    waste += float(model_dict[output][3])
if len(kmec)!=0:
    filter_acc["KMEC"] = round(acc/len(kmec), 2)
    filter_eff["KMEC"] = round(eff/len(kmec), 2)
    filter_wasted["KMEC"] = round(waste/len(kmec), 2)
else:
    filter_acc["KMEC"] = 0
    filter_eff["KMEC"] = 0
    filter_wasted["KMEC"] = 0


filter_labels = ["K", "M", "KM", "KMC", "KME", "KMEC"]
filter_acc_h = [filter_acc["K"], filter_acc["M"], filter_acc["KM"], filter_acc["KMC"], filter_acc["KME"], filter_acc["KMEC"]]
filter_eff_h = [filter_eff["K"], filter_eff["M"], filter_eff["KM"], filter_eff["KMC"], filter_eff["KME"], filter_eff["KMEC"]]
filter_wasted_h = [filter_wasted["K"], filter_wasted["M"], filter_wasted["KM"], filter_wasted["KMC"], filter_wasted["KME"], filter_wasted["KMEC"]]


filter_accc = plt.bar([2*i for i in range(len(filter_labels))], filter_acc_h, tick_label=filter_labels)
plt.ylabel("Accuracy")
plt.title("Accuracy by Filter")
plt.savefig('filter_accuracy.png')
plt.close()

filter_efff = plt.bar([2*i for i in range(len(filter_labels))], filter_eff_h, tick_label=filter_labels)
plt.ylabel("Efficiency (Gen/Min)")
plt.title("Efficiency by Filter")
plt.savefig('filter_efficiency.png')
plt.close()


filter_waste = plt.bar([2*i for i in range(len(filter_labels))], filter_wasted_h, tick_label=filter_labels)
plt.ylabel("% Wasted Generations")
plt.title("% Wastefulness by Filter")
plt.savefig('filter_waste.png')
plt.close()


prompt_acc = {}

acc = 0
for output in zero:
    acc += float(model_dict[output][0])

if len(zero) !=0:
    prompt_acc["Zero-Shot CoT"] = round(acc/len(zero), 2)

else:
    prompt_acc["Zero-Shot CoT"] = 0

acc = 0
for output in one:
    acc += float(model_dict[output][0])
if len(one) > 0:
    prompt_acc["One-Example CoT"] = round(acc/len(one), 2)
else:
    prompt_acc["One-Example CoT"] = 0
    
acc = 0
for output in two:
    acc += float(model_dict[output][0])

if len(two)!=0:
    prompt_acc["Two-Example CoT"] = round(acc/len(two), 2)
else:
    prompt_acc["Two-Example CoT"] = 0

prompt_labels = ["Zero-Shot CoT", "One-Example CoT", "Two-Example CoT"]
prompt_acc_h = [prompt_acc["Zero-Shot CoT"], prompt_acc["One-Example CoT"], prompt_acc["Two-Example CoT"]]

prompt_waste = plt.bar([2*i for i in range(len(prompt_labels))], prompt_acc_h, tick_label=prompt_labels)
plt.ylabel("Accuracy")
plt.title("Accuracy by Prompt")
plt.savefig('prompt_accuracy.png')
plt.close()

greatest = (0, "")
for key in model_dict.keys():
    accuracy = float(model_dict[key][0])
    if accuracy > greatest[0]:
        greatest = (accuracy, key)

n = greatest[1]
if "html" in n:
    model = n[n.index("ate-")+4:n.index("-html")]
else:
    model = n[n.index("ate-")+4:n.index("-pdf")]

with open("most_accurate.txt", "w", encoding="UTF-8") as f:
    f.write(f"Most accurate result is {model} with {accuracy} accuracy, {round(float(model_dict[n][1]),2)} gen/min efficiency, {round(float(model_dict[n][2]),2)} perplexity, and {round(float(model_dict[n][3]),2)} wasted generations.")