What happens if all philosophers take the chopstick on their left at the same time?
-> Personne ne mange, deadlock : chacun a 1 chopstick

What’s the maximum number of philosophers that can eat at the same time?
-> 5//2 = 2, il faut 2 chopsticks et il y en a 5 au total, donc 2 au max mangent en même temps

Although this solution guarantees that no two neighbors are eating simultaneously, it nevertheless must be rejected. Why?
-> Ne garantit pas l'absence de deadlocks si tous les philosophese veulent manger en même temps

Solution de Tanguy : 
```
preuve de la proposition: si les philosophe ne sont pas tous droitier ou tous gaucher il n'y a pas de deadlock.
Il y a deadlock si les 5 philosphes ont une baguette en main et attendent pour l'autre baguette
Prenons le philosophe i, supposons qu'il est gaucher   (il tient la baguette de gauche donc la baguette i et non i+1%5). Si il est droitier au obient le résulat symtérique: tout le monde sera droitier.,
Le philosophe i attend pour la baguette droite (baguette (i+1)%5). Comme le philosophe (i+1)%5 est bloqué, cela veut dire qu'il tient forcément la baguette (i+1)%5 et attend la baguette (i+2)%5, il est donc gaucher aussi.
On peut recommencer le processus avec le philosophe (i+2)%5, (i+3)%5 etc... Tous les philosophes doivent être gaucher.
On a donc montré: deadlock => tous droitiers ou tous gauchers.
Donc par la contraposée: non (tous droitier) et non (tous gauchers) => pas de deadlock
```

Exercice 1:
On définit un ordre de prenage de chopstick : gauche toujours pour 0->3, droite pour 4
Le but étant qu'au moins 1 mange différemment des autres, en prenant l'autre baguette en premier

Exercice 2:
```python
N = 5
chopstick = [Mutex() for i in range(N)]
 
def philosopher(i):
  while True:
      think()
 
      left_stick = i
      right_stick = (i + 1) % N
 
      chopstick[left_stick].acquire()
      chopstick[right_stick].acquire()
 
      eat()
 
      chopstick[left_stick].release()
      chopstick[right_stick].release()
```
