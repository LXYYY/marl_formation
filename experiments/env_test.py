import numpy as np

import multirobot.scenarios as scenarios
from multirobot.environment.environment import MultiAgentEnv
from multirobot.common.cmd_util import parse_args

if __name__ == '__main__':
    # parse arguments
    args = parse_args()

    # load scenario from script
    scenario = scenarios.load(args.scenario).Scenario()
    # create world
    world = scenario.make_world()

    # load the saved landmarks
    # scenario.save(world) -->used to save fixed landmarks
    if args.config_path is not None:
       scenario.load(args.config_path,world)

    # create multiagent environment
    env = MultiAgentEnv(world, scenario.reset_world, scenario.reward, scenario.observation, info_callback=None,
                        shared_viewer=True)

    # render call to create viewer window (necessary only for interactive policies)
    env.render()
    # create interactive policies for each agent
    # policies = [InteractivePolicy(env, i) for i in range(env.n)]
    # execution loop
    obs_n = env.reset()
    while True:
        # query for action from each agent's policy
        act_n = []
        for i in range(env.n):
            # act_n.append(policy.action(obs_n[i]))
            # let it do nothing
            act_n.append(np.array([-0.4, -1]))
        # step environment
        obs_n, reward_n, done_n, _ = env.step(act_n)
        # render all agent views
        env.render()
        # display rewards
        # for agent in env.world.agents:
        #    print(agent.name + " reward: %0.3f" % env._get_reward(agent))

