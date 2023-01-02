# 2/1/2023
# V13.3

import client
from threading import Thread

Thread(target=client.animationInstance.animationThread).start()

def test_empty_queue_during_init():
    assert not client.animationInstance.queue

def test_remove_dupl_animations():
    for i in range(10):
        client.animationInstance.queue.append([6, 0, (173, 216, 230)])

    assert len(client.animationInstance.queue) == 10
    
    # WIP


