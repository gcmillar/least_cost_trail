# Computing least cost path (trail) from one start point to all possible end points (e.g., x=-6486.35675036, y=6748.63899645 to x=1158.18408741, y=6694.93027862; x=835.931780434, y=5047.86293184; x=-703.718130687, y=1628.40789667) given  already calculated friction map (e.g., 'fric'; time penalties—added time to walk 1m) 
 
import grass.script as gscript

def trail(elevation, friction, slope_factor, start_coordinate, end_coordinate, ):
    gscript.run_command('r.walk', flags='k', elevation='elev', friction='fric',\
    					slope_factor=slope_factor, start_coordinates=start_coordinate,\
    					stop_coordinates=end_coordinate, output='walk_cost',\
    					outdir='walk_cost_dir'
    gscript.run_command('r.drain', flags='d' input='walk_cost', output='drain',
    					direction='walk_cost_dir', drain='vect_path',
    					start_coordinates=end_coordinate, env=env)                   
 
if __name__ == '__main__':
    elevation = 'elev'
    friction = 'fric'
    slope_factor = [-0.2125]
    start = [-6486.35675036,6748.63899645]
    end = [1158.18408741,6694.93027862,835.931780434,5047.86293184,-703.718130687,1628.40789667]
    trail(elevation, friction, slope_factor, start, end)
