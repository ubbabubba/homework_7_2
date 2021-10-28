
from pytest_bdd import scenario, given, when, then, scenarios, parsers
from car.car import Car

scenarios('..//features/car.feature')

EXTRA_TYPES = {
    'Number': int,
}


@given(parsers.cfparse('the car speed is "{initial:Number}" miles per hour',
       extra_types=EXTRA_TYPES), target_fixture='new_car')
def new_car(initial):
    return Car(speed=initial)


@when('I accelerate')
def accelerate(new_car):
    new_car.accelerate()

@when('I brake')
def brake(new_car):
    new_car.brake()

@then(parsers.cfparse('the speed is "{speed:Number}" miles per hour', extra_types=EXTRA_TYPES))
def speed_check(new_car, speed):
    assert new_car.say_speed() == speed

