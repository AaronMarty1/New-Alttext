# Google OAuth Login Setup - Complete ✅

## What Was Configured

✅ **django-allauth** installed and configured
✅ **Google OAuth credentials** added to `.env` file
✅ **Site** configured (127.0.0.1:8000)
✅ **Google Social App** created in database
✅ **Login template** updated with Google login button
✅ **All migrations** applied

## How to Use

### For Users:
1. Go to the login page: `http://127.0.0.1:8000/accounts/login/`
2. You'll see a **"Sign in with Google"** button
3. Click it to authenticate with your Google account
4. After authentication, you'll be logged in automatically

### For Production:
1. **Update the Site domain** in Django admin:
   - Go to: `/admin/sites/site/`
   - Change domain from `127.0.0.1:8000` to your production domain
   - Example: `yourdomain.com`

2. **Update Google OAuth Redirect URIs**:
   - Go to: https://console.cloud.google.com/apis/credentials
   - Edit your OAuth 2.0 Client ID
   - Add authorized redirect URI: `https://yourdomain.com/accounts/google/login/callback/`

3. **Update .env file** with production credentials if different

## Configuration Details

### Google OAuth Credentials:
- **Client ID**: `444201951480-rq2c8vrq1rtcsa5pucfss08ptvmm5ov7.apps.googleusercontent.com`
- **Client Secret**: `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`
- Stored in: `.env` file

### Django Settings:
- Authentication method: Email-based
- Username not required
- Email verification: None (can be changed to 'mandatory' if needed)

## Important Notes

⚠️ **For Production:**
- Make sure to update the Site domain
- Add production redirect URI in Google Console
- Use HTTPS in production (required by Google OAuth)

⚠️ **Security:**
- Never commit `.env` file to git (already in `.gitignore`)
- Keep your Client Secret secure
- Rotate credentials if compromised

## Testing

1. **Start the server**:
   ```bash
   python manage.py runserver
   ```

2. **Visit login page**:
   ```
   http://127.0.0.1:8000/accounts/login/
   ```

3. **Click "Sign in with Google"** button

4. **Authenticate** with your Google account

5. **You should be logged in** and redirected to the main page

## Troubleshooting

### Google login button not showing?
- Check that `django-allauth` is in `INSTALLED_APPS`
- Verify migrations are applied
- Check browser console for errors

### "Redirect URI mismatch" error?
- Make sure redirect URI in Google Console matches your site domain
- For local: `http://127.0.0.1:8000/accounts/google/login/callback/`
- For production: `https://yourdomain.com/accounts/google/login/callback/`

### "Invalid client" error?
- Verify Client ID and Secret in `.env` file
- Check that Social App is created in database
- Run the setup script again if needed

## Files Modified

- `alttext/settings.py` - Added allauth configuration
- `alttext/urls.py` - Added allauth URLs
- `templates/registration/login.html` - Added Google login button
- `.env` - Added Google OAuth credentials
- `requirements.txt` - Added django-allauth and dependencies

## Next Steps

✅ Google OAuth is fully configured and ready to use!
✅ Users can now log in with their Google accounts
✅ All existing authentication still works (email/password)

Enjoy your new Google login feature! 🎉

