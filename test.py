double max2 = e > f && e > g ? e : f > g ? f : g;
max2 = max2 > h ? max2 : h;
double min2 = e < f && e < g ? e : f < g ? f : g;
min2 = min2 < h ? min2 : h;
Console.WriteLine("Largest :" + (a > b && a > c ? a : b > c ? b : c) + "\n");
    Console.WriteLine("smallest :" + (a > b && a > c ? a : b > c ? b : c) + "\n");