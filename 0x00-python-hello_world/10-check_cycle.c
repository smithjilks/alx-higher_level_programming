#t = list->next;
p2 = p2->next->next;

if (list == p2)
  {
    list = prev;
    prev =  p2;
    while (1)
      {
	p2 = prev;
	while (p2->next != list && p2->next != prev)
	  {
	    p2 = p2->next;
	  }
	if (p2->next == list)
	  break;

	list = list->next;
      }
    return (1);
  }
}

return (0)
2021 GitHub, Inc.;
}
