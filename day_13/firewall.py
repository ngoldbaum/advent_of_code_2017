class Layer:
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.scanner_step = 1
        self.occupied = False
        if self.range > 0:
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
    def __init__(self, layer_info):
        used_layers = [l[0] for l in layer_info]
        n_layers = max(used_layers) + 1
        self.layers = []
        self.time = 0
        for i in range(n_layers):
            if i in used_layers:
                app = Layer(i, layer_info[used_layers.index(i)][1])
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

    def run(self):
        severity = 0
        for layer in self.layers:
            layer.occupied = True
            if layer.caught():
                severity += layer.depth * layer.range
            self.step()
            self.time += 1
            layer.occupied = False
        return severity


if __name__ == "__main__":

    with open('input', 'r') as f:
        text = f.readlines()

    text = [t.strip().split(': ') for t in text]
    layer_info = [[int(t[0]), int(t[1])] for t in text]

    fw = Firewall(layer_info)
    print(fw.run())
