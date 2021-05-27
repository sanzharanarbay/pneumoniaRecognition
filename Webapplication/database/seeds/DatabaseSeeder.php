<?php

use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
         $this->call(UsersTableSeeder::class);
        $this->call(PatientTableSeeder::class);
        $this->call(DoctorTableSeeder::class);
        $this->call(StaffTableSeeder::class);
        $this->call(InpatientTableSeeder::class);
        $this->call(AppointmentTableSeeder::class);
         $this->call(SettingsTableSeeder::class);

    }
}