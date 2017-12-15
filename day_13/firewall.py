class Layer:
    def __init__(self, depth, range, scanner_pos=None, scanner_step=None):
        self.depth = depth
        self.range = range
        if scanner_step is not None:
            self.scanner_step = scanner_step
        else:
            self.scanner_step = 1
        self.occupied = False
        if self.range > 0:
            if scanner_pos is not None:
                self.scanner_pos = scanner_pos
            else:
                self.scanner_pos = 0

    def __str__(self):
        ret = str(self.depth) + ": "
        if self.range == 0:
            if self.occupied:
                return ret + "(.)"
            else:
                return ret + "..."
        for i in range(self.range):
            if self.occupied and i == 0:
                if i == self.scanner_pos:
                    ret += "(S)"
                else:
                    ret += "( )"
            else:
                if i == self.scanner_pos:
                    ret += "[S]"
                else:
                    ret += "[ ]"
        return ret

    def step(self):
        if self.range == 0:
            return
        if (((self.scanner_pos == self.range - 1 and self.scanner_step == 1) or
             (self.scanner_pos == 0 and self.scanner_step == -1))):
            self.scanner_step *= -1
        self.scanner_pos += self.scanner_step

    def caught(self):
        return self.occupied and self.range > 0 and self.scanner_pos == 0


class Firewall:
    def __init__(self, layer_info, time=None):
        used_layers = [l[0] for l in layer_info]
        n_layers = max(used_layers) + 1
        self.layers = []
        if time is not None:
            self.time = time
        else:
            self.time = 0
        for i in range(n_layers):
            if i in used_layers:
                info = layer_info[used_layers.index(i)]
                app = Layer(*info)
            else:
                app = Layer(i, 0)
            self.layers.append(app)

    def __str__(self):
        return (str(self.time) + "\n" +
                "\n".join([str(layer) for layer in self.layers]) + "\n")

    def step(self):
        """Evolve states of security bots by one timestep"""
        for layer in self.layers:
            layer.step()

    def layer_info(self):
        layer_info = []
        for layer in self.layers:
            if layer.range > 0:
                layer_info.append([layer.depth, layer.range,
                                   layer.scanner_pos, layer.scanner_step])
        return layer_info

    def run(self):
        first = True
        layer_info = None
        for layer in self.layers:
            layer.occupied = True
            if layer.caught():
                return layer_info, False
            self.step()
            if first:
                layer_info = self.layer_info()
                first = False
            self.time += 1
            layer.occupied = False
        return layer_info, True


if __name__ == "__main__":

    with open('input', 'r') as f:
        text = f.readlines()

    text = [t.strip().split(': ') for t in text]
    layer_info = [[int(t[0]), int(t[1])] for t in text]

    state = layer_info
    test_time = 0

    while True:
        if test_time % 1000 == 0:
            print(test_time)
        fw = Firewall(state, test_time)
        state, success = fw.run()
        if success:
            print(test_time)
            break
        if state is None:
            fw.step()
            state = fw.layer_info()
        test_time += 1
