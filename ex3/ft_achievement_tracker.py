if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    names = ["alice", "bob", "charlie"]
    arr = [alice, bob, charlie]
    
    i = 0
    while i < 3:        
        print(f"Player {names[i]} achievements: {arr[i]}")
        i+=1

    print()     
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {alice.union(bob, charlie)}")
    print(f"Total unique achievements: {len(alice.union(bob, charlie))}")
    print()
    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    
    alice_diff = alice.difference(bob, charlie)
    bob_diff = bob.difference(alice, charlie)
    charlie_diff = charlie.difference(alice, bob)
    
    print(f"Rare achievements (1 player): "
          f"{alice_diff.union(bob_diff, charlie_diff)}")
    print()
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")