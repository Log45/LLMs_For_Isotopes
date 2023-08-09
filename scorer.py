
with open("results.csv", "r", encoding="UTF-8") as f:
    output_lst = []
    model_dict = {}
    for line in f:
        if "filename" in line:
            pass
        else:
            #filename,score,total generations,total time,efficiency (gen/min),perplexity score,relevant generations,percent of relevant generations generated,wasted generations,parser
            name, acc, gens, time, eff, perp, relgen, percrelgen, wasted, parser = line.strip().split(",")
            print(name)
            model_dict[name] = (acc, eff, perp, wasted/gens)