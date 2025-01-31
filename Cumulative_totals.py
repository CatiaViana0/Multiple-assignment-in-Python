if __name__ == '__main__' :
    Shop_Cli = (("A.Pinto", "Loja_A", "12/02/20", 60),
                   ("E.Gomes", "Loja_B", "10/02/20", 120),
                   ("A.Pinto", "Loja_A", "08/02/20", 68),
                   ("E.Gomes", "Loja_B", "07/02/20", 75),
                   ("A.Pinto", "Loja_A", "10/02/20", 50),
                   ("E.Gomes", "Loja_B", "09/02/20", 24),
                   ("A.Pinto", "Loja_A", "04/02/20", 26),
                   ("E.Gomes", "Loja_B", "04/02/20", 120),
                   ("A.Pinto", "Loja_A", "25/02/20", 24))
    Name="A.Pinto"
    Tuples_ByDate = sorted(Shop_Cli, key = lambda x: x[2])
    Total = 0
    TotalsList = []
    for I in range(0,len(Tuples_ByDate)):
        if Name == Tuples_ByDate[I][0]:
            Total = Total+Tuples_ByDate[I][3]
            TotalsList.append((Tuples_ByDate[I][2], Total))
    print(f"Totals accumulated by {Name}= {TotalsList}")
