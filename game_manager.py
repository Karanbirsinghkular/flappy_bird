import random

import pipe


class Game_manager:
    def __init__(self, bird, pipe_velx, pipe_dist_ll, pipe_dist_ul, pipe_color,
                 w, h, lower_space_limit, upper_space_limit, breadth_ll, breadth_ul):
        self.score = 0
        self.bird = bird
        self.pipe_velx = pipe_velx
        self.pipe_dist_ll = pipe_dist_ll
        self.pipe_dist_ul = pipe_dist_ul
        self.pipe_color = pipe_color
        self.pipelist_maxlen = 5
        self.pipelist = []
        self.w = w
        self.h = h
        self.lower_space_limit = lower_space_limit
        self.upper_space_limit = upper_space_limit
        self.breadth_ll = breadth_ll
        self.breadth_ul = breadth_ul
        rand = random.Random()
        space = rand.randint(lower_space_limit, upper_space_limit)
        self.pipelist.append(pipe.Pipe(w, rand.randint(0, h - space), rand.randint(self.breadth_ll, self.breadth_ul), space, w, h, pipe_color))
        for i in range(self.pipelist_maxlen - 1):
            space = rand.randint(lower_space_limit, upper_space_limit)
            self.pipelist.append(
                pipe.Pipe(self.pipelist[i].posx + self.pipelist[i].breadth +
                          rand.randint(self.pipe_dist_ll, self.pipe_dist_ul), rand.randint(0, h - space),
                          rand.randint(self.breadth_ll, self.breadth_ul), space, w, h,
                          pipe_color))


    def addPipe(self):
        rand = random.Random()
        space = rand.randint(self.lower_space_limit, self.upper_space_limit)
        # print(self.pipelist[len(self.pipelist) - 1].posx)
        self.pipelist.append(pipe.Pipe(self.pipelist[len(self.pipelist) - 1].posx + self.pipelist[len(self.pipelist) - 1].breadth + rand.randint(self.pipe_dist_ll, self.pipe_dist_ul), rand.randint(0, self.h - space), rand.randint(self.breadth_ll, self.breadth_ul), space, self.w, self.h,
                          self.pipe_color))

    def removePipe(self, pipe):
        self.updatescore(pipe)
        self.pipelist.remove(pipe)

    def update(self, dt):
        self.bird.setAlive(self.isAlive())
        if not self.bird.getAlive():
            self.bird.applyForce(0.025)
            self.bird.update(dt)
            return
        self.bird.update(dt)
        for each in self.pipelist:
            each.update(self.pipe_velx, dt)
            if not each.checkinbounds():
                self.removePipe(self.pipelist[0])
                self.addPipe()

    def birdjump(self, forcey, angvel):
        self.bird.jump(forcey, angvel)

    def show(self, screen):
        for each in self.pipelist:
            each.show(screen)
        self.bird.show(screen)

    def isAlive(self):
        if self.bird.checkinbounds():
            for each in self.pipelist:
                if each.checkinpipe(self.bird):
                    return False
            return True

    def updatescore(self, pipe):
        if self.bird.posx > pipe.posx + pipe.breadth:
            self.score += 1