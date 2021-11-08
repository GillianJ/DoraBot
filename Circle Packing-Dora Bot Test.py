#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


# In[ ]:


import math


# In[ ]:


import sys


# In[ ]:


get_ipython().system('pip --version')


# In[ ]:


get_ipython().system('pip install pygame')


# In[ ]:


import pygame


# In[ ]:


W, H = 1920, 1080


# In[ ]:


HW, HH = W /2, H / 2


# In[ ]:


AREA = W * H


# In[ ]:





# In[ ]:


class circle :
    def _init_(self, x, y, id):
        self.x = x
        self.y = y
        self.radius = 2
        seld.id = id
        self.active = True    


# In[ ]:


circles = list ([])


# In[ ]:


find_space_attempts = 0


# In[ ]:


max_find_space_attempt = 10000


# In[ ]:


exit = False


# In[ ]:


gap = 3


# In[ ]:





# In[ ]:


area_covered = 0.0


# In[ ]:


percentage_coverage = 0


# In[ ]:


last_reported_percentage = -1


# In[ ]:





# In[ ]:


while True:
    while True: 
        x = random.randint(0, W - 1)
        y = random.randint(0, H - 1)
        
        found_space = True
        for c in circles:
            distance = math.hypot(c.x - x, c.y - y)
            if distance <= c.radius + gap:
                found_space = False
                break        
        if found_space: break
            find_space_attempt +=1
            if find_space_attempts >= max_find_space_attempts:
            exit = True
            break
            
    if exit: break
    circles.append(circle(x, y, len(circles)))
    
    for c in circles:
        if not c.active: continue
            for c in circles:
                if c.id == C.id: continue 
                    
                    distance_between_circles = math.hypot(c.x - C.x, c.y - C.y)
                    combined_radius = c.radius + C.radius
                    
                    if distance_between_circles - combined_radius <= gap:
                        c.active = False
                        C.active = False
                        
                        area_covered += (c.radius **2) + math.pi
                        percentage_covered = int((area_covered / AREA) * 100)
                        If last_percentage_covered !=percentage_covered:
                            print percentage_covered
                            last_reported_percentage = percentage_covered 
                        break
                        
            if c.active: c.radius += 1 


# In[ ]:


print "Circles Generated!"
print " Saving File."
image = pygame.Surface(W, H)
for c in circles:
    pygame.draw.circle(image, (255, 255, 255), (c.x, c.y), c.radius,1)
    pygame.image.save(image, "circles.png")
    print"Done"


# In[ ]:




