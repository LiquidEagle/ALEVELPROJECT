    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
      jumping = True

    if jumping:
      y_position -= y_velocity
      y_velocity -= y_gravity
      if y_velocity < -JUMP_HEIGHT:
        jumping = false
        y_velocity = jump_height
      screen.blit(jumping_img, (self.x, self.y)) 
    else:
      #user.drawL() 