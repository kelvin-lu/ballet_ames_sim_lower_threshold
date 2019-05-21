#!/usr/bin/env python

if __name__ == '__main__':

    from ballet.util.log import enable
    from ballet.validation.main import validate

    import ballet_ames_sim_lower_threshold

    enable(level='DEBUG', echo=False)
    validate(ballet_ames_sim_lower_threshold)
